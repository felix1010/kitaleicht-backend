CREATE SCHEMA `kitaleicht` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE `kitaleicht`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `kita` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

INSERT INTO `kitaleicht`.`users` (`kita`, `email`, `password`, `name`) VALUES ('Barleber Schlümpfer', 'freke@gmail.com', 'asdfghjkl', 'Frau Freke');
