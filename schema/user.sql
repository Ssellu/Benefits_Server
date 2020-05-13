CREATE TABLE IF NOT EXISTS tbl_user(
    u_no                  INT              NOT NULL    AUTO_INCREMENT ,
    u_type                INT              NOT NULL    ,
    u_password            VARCHAR(128)     NOT NULL    ,
    u_email               VARCHAR(40)      NOT NULL    ,
    u_cards               VARCHAR(2000)    NULL        ,
    u_last_password_time  DATETIME         NULL        ,
    u_last_accessed_time  DATETIME         NULL        ,
    u_confirm             BOOLEAN          DEFAULT FALSE,
    PRIMARY KEY (u_no)
);
--------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS tbl_auth(
    u_guid          VARCHAR(45)     NOT NULL,
    u_no            INT,
    u_type          INT             NOT NULL,
    u_token         VARCHAR(128)    NOT NULL,
    u_expired_time  DATETIME        NOT NULL
);
--------------------------------------------------------------------
IF NOT EXISTS (
    SELECT CONSTRAINT_NAME
    FROM information_schema.TABLE_CONSTRAINTS
    WHERE
        CONSTRAINT_SCHEMA = DATABASE() AND
        CONSTRAINT_NAME   = 'FK_tbl_auth_u_id_tbl_user_u_id' AND
        CONSTRAINT_TYPE   = 'FOREIGN KEY'
)
THEN
    ALTER TABLE tbl_auth
    ADD CONSTRAINT FK_tbl_auth_u_id_tbl_user_u_id
    FOREIGN KEY(u_no)
    REFERENCES tbl_user (u_no)
    ON DELETE RESTRICT ON UPDATE RESTRICT;
END IF
--------------------------------------------------------------------
-- DROP PROCEDURE IF EXISTS pr_create_tbl_user;

DELIMITER //
CREATE PROCEDURE IF NOT EXISTS pr_create_tbl_user(
    IN p_email varchar(40)  CHARACTER SET 'utf8',
    IN p_password varchar(128)  CHARACTER SET 'utf8'
)

BEGIN
    IF ( select exists(select TRUE from tbl_user where u_email = p_email) ) THEN
            select FALSE;
    ELSE
        insert into tbl_user (
            u_email,
            u_type,
            u_password,
            u_last_password_time,
            u_last_accessed_time
        ) values (
            p_email,
            0,
            p_password,
            SYSDATE(),
            SYSDATE()
        );
        commit;
        SELECT TRUE;
    END IF;
END;//



