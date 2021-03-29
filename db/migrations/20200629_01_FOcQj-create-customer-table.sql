CREATE TABLE customer (
    id              CHAR(36)    NOT NULL,
    first_name      VARCHAR(50) NOT NULL,
    last_name       VARCHAR(50) NOT NULL,
    middle_initial  VARCHAR(1)  NULL,
    created_at      TIMESTAMP   NOT NULL    DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id));