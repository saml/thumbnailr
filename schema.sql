drop table if exists imgs;

create table imgs(
    id integer primary key autoincrement,
    path string not null unique
);

drop index if exists index_imgs_path;
create index index_imgs_path on imgs ( path );


drop table if exists renditions;

create table renditions(
    img_id integer,
    name string,
    crop_x integer,
    crop_y integer,
    crop_width integer,
    crop_height integer,
    width integer,
    height integer,
    primary key(img_id, name)
);
