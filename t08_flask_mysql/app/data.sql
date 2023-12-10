DROP TRIGGER IF EXISTS AfterUpdateRentalAgency;

DELIMITER //
CREATE TRIGGER AfterUpdateRentalAgency
AFTER UPDATE
ON rental_agency FOR EACH ROW
BEGIN
    INSERT INTO RentalAgencyCopy(IDRentalAgency, OldHead, newHead, OldPhone, newPhone, Action, TimeStamp,User)
    VALUES(OLD.Id, OLD.rental_agency_head, NEW.rental_agency_head, OLD.phone, NEW.phone, 'update', NOW(), User());
END //
DELIMITER ;

DROP TRIGGER IF EXISTS AfterDeleteLocationMin6Row;

DELIMITER //
CREATE TRIGGER AfterDeleteLocationMin6Row
AFTER DELETE
ON location FOR EACH ROW
BEGIN
	IF(SELECT COUNT(*) FROM location) < 6
    THEN SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Delete error MIN cardinality';
	END IF;
END //
DELIMITER ;

DROP TRIGGER IF EXISTS PreventRentUpdate;

DELIMITER //
CREATE TRIGGER PreventRentUpdate
BEFORE UPDATE
ON rent FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Modification of data in the rent table is not allowed.';
END //
DELIMITER ;

DELIMITER //
CREATE FUNCTION AveragePriceRent()
RETURNS DECIMAL(8,2)
BEGIN
	RETURN(SELECT AVG(total_price) From Rent)
END
DELIMITER ;


DELIMITER //
CREATE PROCEDURE AVERAGE_RENT_PRICE()
BEGIN
	SELECT AveragePriceRent();
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS CreateDynamicTableFromClient;

DELIMITER //
CREATE PROCEDURE CreateDynamicTableFromClient()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE firstNameValue VARCHAR(45);
    DECLARE lastNameValue VARCHAR(45);
    DECLARE tableName VARCHAR(255);
    DECLARE timestampFormat VARCHAR(20);

    DECLARE clientCursor CURSOR
    FOR SELECT first_name, last_name FROM client;

    DECLARE CONTINUE HANDLER
    FOR NOT FOUND SET done = TRUE;

	SET timestampFormat = DATE_FORMAT(NOW(), '%Y_%m_%d');
    OPEN clientCursor;
    MyLoop: LOOP
        FETCH clientCursor INTO firstNameValue, lastNameValue;

        IF done THEN LEAVE MyLoop;
        END IF;
        SET tableName = CONCAT(firstNameValue, '_', lastNameValue, '_', timestampFormat);
		SET @sql_query = CONCAT('CREATE TABLE ', tableName, ' (age INT, email VARCHAR(75), phone VARCHAR(45))');

        PREPARE stmt FROM @sql_query;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP;
    CLOSE clientCursor;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS InsertValueIntoClient;

DELIMITER //
CREATE PROCEDURE InsertValueIntoClient(
    in_first_name VARCHAR(45),
    in_last_name VARCHAR(45),
    in_phone VARCHAR(45),
    in_email VARCHAR(45),
    in_age INT,
    in_driver_license VARCHAR(45)
)
BEGIN
    INSERT INTO client (first_name, last_name, phone, email, age, driver_license)
    VALUES (in_first_name, in_last_name, in_phone, in_email, in_age, in_driver_license);
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS Insert10ValuesIntoCountry;

DELIMITER //
CREATE PROCEDURE Insert10ValuesIntoCountry()
BEGIN
    DECLARE loopCounter INT DEFAULT 0;
    DECLARE countryName VARCHAR(255);
    DECLARE count INT;


    SET count = (SELECT MAX(ID) FROM Country);
    WHILE loopCounter < 10 DO
        SET loopCounter = loopCounter + 1;
        SET count = count + 1;
        SET countryName = CONCAT('CountryName#', count);
        INSERT INTO country (name) VALUES (countryName);
    END WHILE;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS InsertIntoManyToManyTable;

DELIMITER //
CREATE PROCEDURE InsertIntoManyToManyTable(rent_id_param INT, option_id_param INT)
BEGIN
	IF
	   EXISTS(SELECT Id FROM Rent WHERE id = rent_id_param) AND
       EXISTS(SELECT id FROM lab_4_shema.Option Where id = option_id_param)
    THEN
		INSERT INTO Rent_option (rent_id,option_id) VALUES (rent_id_param,option_id_param);
	ELSE
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = "Rent_id or Option_id incorrect";
	END IF;
END //
DELIMITER ;

CREATE TABLE ArbitraryTableManyToOne (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    country_id INT
);

DELIMITER //
CREATE TRIGGER CheckCorrectForeignKey
BEFORE INSERT
ON ArbitraryTableManyToOne FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT Id FROM Country WHERE Id = NEW.country_id)
    THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Country_id dont exist';
    END IF;
END //
DELIMITER ;
