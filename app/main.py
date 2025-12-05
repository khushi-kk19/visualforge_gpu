# from flask import Flask, request, jsonify, send_file
# from detector import ObjectDetector
# from image_editor import ImageEditor
# import os

# app = Flask(__name__)
# app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max

# detector = ObjectDetector("yolov8n.pt")
# editor = ImageEditor()
# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route('/detect', methods=['POST'])
# def detect():
#     """Detect objects in uploaded image"""
#     if 'image' not in request.files:
#         return jsonify({"error": "No image provided"}), 400
    
#     file = request.files['image']
#     filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(filepath)
    
#     detections = detector.detect_objects(filepath)
#     objects = list(set([d["object"] for d in detections]))
    
#     return jsonify({
#         "detected_objects": objects,
#         "detections": detections
#     })

# @app.route('/remove', methods=['POST'])
# def remove_object():
#     """Remove object from image"""
#     if 'image' not in request.files or 'object' not in request.form:
#         return jsonify({"error": "Missing image or object name"}), 400
    
#     file = request.files['image']
#     object_name = request.form['object']
#     filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(filepath)
    
#     output = editor.remove_object(filepath, object_name)
#     return send_file(output, mimetype='image/png')

# @app.route('/replace', methods=['POST'])
# def replace_object():
#     """Replace object with another"""
#     if 'image' not in request.files or 'old' not in request.form or 'new' not in request.form:
#         return jsonify({"error": "Missing parameters"}), 400
    
#     file = request.files['image']
#     old_obj = request.form['old']
#     new_obj = request.form['new']
#     filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(filepath)
    
#     output = editor.replace_object(filepath, old_obj, new_obj)
#     return send_file(output, mimetype='image/png')

# @app.route('/add', methods=['POST'])
# def add_object():
#     """Add new object to image"""
#     if 'image' not in request.files or 'object' not in request.form:
#         return jsonify({"error": "Missing parameters"}), 400
    
#     file = request.files['image']
#     new_obj = request.form['object']
#     filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(filepath)
    
#     output = editor.add_object(filepath, new_obj)
#     return send_file(output, mimetype='image/png')

# @app.route('/style', methods=['POST'])
# def apply_style():
#     """Change image style"""
#     if 'image' not in request.files or 'style' not in request.form:
#         return jsonify({"error": "Missing parameters"}), 400
    
#     file = request.files['image']
#     style = request.form['style']
#     filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(filepath)
    
#     output = editor.change_style(filepath, style)
#     return send_file(output, mimetype='image/png')

# @app.route('/generate', methods=['POST'])
# def generate_variations():
#     """Generate variations"""
#     if 'image' not in request.files:
#         return jsonify({"error": "No image provided"}), 400
    
#     file = request.files['image']
#     filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(filepath)
    
#     variations = editor.generate_variations(filepath)
#     return jsonify({"variations": variations})

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)
# from flask import Flask, request, jsonify, send_file
# from detector import ObjectDetector
# from image_editor import ImageEditor
# import os
# import sys

# # Add parent directory to path
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# app = Flask(__name__)
# app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max

# detector = ObjectDetector("yolov8n.pt")
# editor = ImageEditor()
# UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "uploads")
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route('/detect', methods=['POST'])
# def detect():
#     """Detect objects in uploaded image"""
#     try:
#         if 'image' not in request.files:
#             return jsonify({"error": "No image provided"}), 400
        
#         file = request.files['image']
#         if file.filename == '':
#             return jsonify({"error": "No file selected"}), 400
        
#         filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#         file.save(filepath)
        
#         print(f"Processing image: {filepath}")
#         detections = detector.detect_objects(filepath)
#         objects = list(set([d["object"] for d in detections]))
        
#         return jsonify({
#             "detected_objects": objects,
#             "detections": detections,
#             "status": "success"
#         })
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/remove', methods=['POST'])
# def remove_object():
#     """Remove object from image"""
#     try:
#         if 'image' not in request.files or 'object' not in request.form:
#             return jsonify({"error": "Missing image or object name"}), 400
        
#         file = request.files['image']
#         object_name = request.form['object']
#         filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#         file.save(filepath)
        
#         output = editor.remove_object(filepath, object_name)
#         return send_file(output, mimetype='image/png')
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/replace', methods=['POST'])
# def replace_object():
#     """Replace object with another"""
#     try:
#         if 'image' not in request.files or 'old' not in request.form or 'new' not in request.form:
#             return jsonify({"error": "Missing parameters"}), 400
        
#         file = request.files['image']
#         old_obj = request.form['old']
#         new_obj = request.form['new']
#         filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#         file.save(filepath)
        
#         output = editor.replace_object(filepath, old_obj, new_obj)
#         return send_file(output, mimetype='image/png')
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/add', methods=['POST'])
# def add_object():
#     """Add new object to image"""
#     try:
#         if 'image' not in request.files or 'object' not in request.form:
#             return jsonify({"error": "Missing parameters"}), 400
        
#         file = request.files['image']
#         new_obj = request.form['object']
#         filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#         file.save(filepath)
        
#         output = editor.add_object(filepath, new_obj)
#         return send_file(output, mimetype='image/png')
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/style', methods=['POST'])
# def apply_style():
#     """Change image style"""
#     try:
#         if 'image' not in request.files or 'style' not in request.form:
#             return jsonify({"error": "Missing parameters"}), 400
        
#         file = request.files['image']
#         style = request.form['style']
#         filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#         file.save(filepath)
        
#         output = editor.change_style(filepath, style)
#         return send_file(output, mimetype='image/png')
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)
from flask import Flask, request, jsonify, send_file, render_template
from detector import ObjectDetector
from image_editor import ImageEditor
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
            static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

detector = ObjectDetector("yolov8n.pt")
editor = ImageEditor()
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    """Detect objects in uploaded image"""
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image provided"}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        
        print(f"Processing image: {filepath}")
        detections = detector.detect_objects(filepath)
        objects = list(set([d["object"] for d in detections]))
        
        return jsonify({
            "detected_objects": objects,
            "detections": detections,
            "status": "success"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/remove', methods=['POST'])
def remove_object():
    """Remove object from image"""
    try:
        if 'image' not in request.files or 'object' not in request.form:
            return jsonify({"error": "Missing image or object name"}), 400
        
        file = request.files['image']
        object_name = request.form['object']
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        
        output_path = os.path.join(UPLOAD_FOLDER, "output_removed.png")
        editor.remove_object(filepath, object_name, output_path)
        
        return send_file(output_path, mimetype='image/png', as_attachment=True, download_name='output_removed.png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/replace', methods=['POST'])
def replace_object():
    """Replace object with another"""
    try:
        if 'image' not in request.files or 'old' not in request.form or 'new' not in request.form:
            return jsonify({"error": "Missing parameters"}), 400
        
        file = request.files['image']
        old_obj = request.form['old']
        new_obj = request.form['new']
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        
        output_path = os.path.join(UPLOAD_FOLDER, "output_replaced.png")
        editor.replace_object(filepath, old_obj, new_obj, output_path)
        
        return send_file(output_path, mimetype='image/png', as_attachment=True, download_name='output_replaced.png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/add', methods=['POST'])
def add_object():
    """Add new object to image"""
    try:
        if 'image' not in request.files or 'object' not in request.form:
            return jsonify({"error": "Missing parameters"}), 400
        
        file = request.files['image']
        new_obj = request.form['object']
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        
        output_path = os.path.join(UPLOAD_FOLDER, "output_added.png")
        editor.add_object(filepath, new_obj, output_path)
        
        return send_file(output_path, mimetype='image/png', as_attachment=True, download_name='output_added.png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/style', methods=['POST'])
def apply_style():
    """Change image style"""
    try:
        if 'image' not in request.files or 'style' not in request.form:
            return jsonify({"error": "Missing parameters"}), 400
        
        file = request.files['image']
        style = request.form['style']
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        
        output_path = os.path.join(UPLOAD_FOLDER, "output_styled.png")
        editor.change_style(filepath, style, output_path)
        
        return send_file(output_path, mimetype='image/png', as_attachment=True, download_name='output_styled.png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)