import thumbnailr
from thumbnailr import IMG_DIR, PREFIX_ORIGINAL, PARAM_FILE

app = thumbnailr.app

class ImagePath(object):
    def __init__(self, img_path,
            img_dir=IMG_DIR,
            prefix_original=PREFIX_ORIGINAL):
        '''image path

        >>> img = ImagePath('foo/bar.jpg', base_dir='/tmp/imgs', prefix_original='original')
        >>> img.ext == '.jpg'
        True
        >>> img.path == '/tmp/imgs/foo/bar.jpg'
        True
        >>> img.original == '/tmp/imgs/foo/bar.jpg/original.jpg'
        True
        '''

        _,self.ext = os.path.splitext(img_path)
        self.path = os.path.join(img_dir, img_path)
        self.original = os.path.join(self.path, prefix_original + self.ext)


@app.route('/<path:img_path>/<int:width>x<int:height>.<ext>')
def rendition_handler(img_path, width, height, ext):
    return '''%s
%d x %d .%s''' % (img_path, width, height, ext)


@app.route('/<path:img_path>/upload', methods=['GET'])
def image_upload_form(img_path):
    return flask.render_template('upload_form.html', img_path=img_path, base_dir=IMG_DIR, param_file=PARAM_FILE)


@app.route('/<path:img_path>', methods=['POST', 'GET'])
def image_handler(img_path):
    img = ImagePath(img_path)

    if 'POST' == flask.request.method:
        f = flask.request.files[PARAM_FILE]

        if os.path.exists(img.path):
            shutil.rmtree(img.path)

        os.makedirs(img.path)
        f.save(img.original)

        return 'saved: ' + img.original

    # GET
    if not os.path.exists(img.original):
        flask.abort(404)
        return
    return flask.send_file(img.original)



