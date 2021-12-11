CREATE TABLE `customer` (
	`id` varchar(8) NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`currently_borrowing` varchar(12),
	`due_date` DATE,
	PRIMARY KEY (`id`)
);

CREATE TABLE `book` (
	`id` varchar(12) NOT NULL,
	`title` varchar(255) NOT NULL,
	`author` varchar(255) NOT NULL,
	`category` varchar(12) NOT NULL,
	`available` BOOLEAN NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `transaction` (
	`book_id` varchar(12) NOT NULL,
	`customer_id` varchar(8) NOT NULL,
	`borrow_date` DATETIME NOT NULL,
	`return_date` DATETIME
);

ALTER TABLE `customer` ADD CONSTRAINT `customer_fk0` FOREIGN KEY (`currently_borrowing`) REFERENCES `book`(`id`);

ALTER TABLE `transaction` ADD CONSTRAINT `transaction_fk0` FOREIGN KEY (`book_id`) REFERENCES `book`(`id`);

ALTER TABLE `transaction` ADD CONSTRAINT `transaction_fk1` FOREIGN KEY (`customer_id`) REFERENCES `customer`(`id`);




