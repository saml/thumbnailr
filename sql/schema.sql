CREATE TABLE images (
    id bigserial PRIMARY KEY,
    url varchar(256) UNIQUE NOT NULL,-- for example, /imgs/some/image.jpg
    width integer NOT NULL,         
    height integer NOT NULL,
    metadata text,                  -- exif and other metadata as JSON
    description text               -- comments about the image. "red shoes!"
);

CREATE INDEX images_description_index ON images (description);

CREATE TABLE renditions (
    url varchar(256) PRIMARY KEY,
    original bigint REFERENCES images (id),
    width integer NOT NULL,
    height integer NOT NULL,
    is_crop boolean NOT NULL,
    crop_x integer,
    crop_y integer,
    crop_w integer,
    crop_h integer,
    description text
);

CREATE INDEX renditions_description_index ON renditions (description);

