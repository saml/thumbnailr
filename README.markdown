# Thumbnailr

You can upload images and generate renditions (thumbnails).

# Upload image

    POST /some/image.jpg
    <<file>>

* rm -rf `<imgdir>/some/image.jpg` if exists.
* mkdir -p `<imgdir>/some/image.jpg`
* cp `<<file>>` `<imgdir>/some/image.jpg/original.jpg`
* calculates rendition crop coordinates according to pre-defined set of renditions and saves.

# Delete image

    DELETE /some/image.jpg

* rm -rf `<imgdir>/some/image.jpg`
* remove crop coordinates for all renditions for image.jpg.

# New rendition

    POST /some/image.jpg/100x200.jpg
    <<file>>

* cp `<<file>>` `<imgdir>/some/image.jpg/100x200.jpg` (replaces existing).

# Edit rendition (can be used to create new rendition, too)

    POST /some/image.jpg/100x200.jpg
    x=0
    y=10
    w=2000
    h=4000

* saves new crop coordinate (x,y,w,h) for 100x200.jpg rendition.
* rm `<imgdir>/some/image.jpg/100x200.jpg` if exists.

# Generate rendition

    GET /some/image.jpg/100x200.jpg

* serve `<imgdir>/some/image.jpg/100x200.jpg` if exists. done.
* 404 if `<imgdir>/some/image.jpg/original.jpg` does not exist. (or get it from origin server).
* read (X,Y,W,H,100,200) for 100x200.jpg. If not found, calculate (X,Y,W,H).
* convert `<imgdir>/some/image.jpg/original.jpg` -crop WxH+X+Y -resize 100x200 `<imgdir>/some/image.jpg/100x200.jpg`
* serve `<imgdir>/some/image.jpg/100x200.jpg`.

# Delete rendition

    DELETE /some/image.jpg/100x200.jpg

* rm `<imgdir>/some/image.jpg/100x200.jpg`
* removes crop coordinates for 100x200.jpg.
