-- creat a TABLE and insert multiple values to the created DB second_table.
CREATE TABLE IF NOT EXISTS `seccond_table` (`id` INT, `name` VARCHAR(256), `score` INT);
INSERT INTO `second_table` (`id`,`name`,`score`) VALUES (1, "John", 10);
INSERT INTO `second_table` (`id`,`name`,`score`) VALUES (2, "Alex", 3);
INSERT INTO `second_table` (`id`,`name`,`score`) VALUES (3, "Bob", 14);
INSERT INTO `second_table` (`id`,`name`,`score`) VALUES (4, "George",8);
