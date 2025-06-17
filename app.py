from bottle import run, route, template, static_file
import cloudinary
import cloudinary.api
import cloudinary.uploader
import json

# Cloudinary config
cloudinary.config(
    cloud_name='dfqreujbo',
    api_key='467879367759351',
    api_secret='tgJspwPABIOzKQrG3YSeb7YAx2g',
    secure=True
)

# === CONFIG ===
target_folder = 'FirstXV14-06'
prefix_filter = 'Lightroom_-_'

# === STEP 1: Move images into folder ===
def move_images_to_folder():
    try:
        result = cloudinary.api.resources(type='upload', prefix=prefix_filter, max_results=100)
        resources = result['resources']
        print(f"Found {len(resources)} image(s) starting with '{prefix_filter}'")

        for item in resources:
            public_id = item['public_id']
            # Skip already moved ones
            if public_id.startswith(f"{target_folder}/"):
                print(f"Skipped {public_id} (already in folder)")
                continue

            new_id = f"{target_folder}/{public_id}"
            try:
                cloudinary.uploader.rename(public_id, new_id)
                print(f"✅ Moved {public_id} -> {new_id}")
            except Exception as e:
                print(f"❌ Failed to move {public_id}: {e}")

    except Exception as e:
        print("❌ Error fetching resources:", e)

# === STEP 2: Get URLs from folder ===
def list_urls_in_folder():
    try:
        result = cloudinary.api.resources(type='upload', prefix=f'{target_folder}/', max_results=100)
        urls = [item['secure_url'] for item in result['resources']]
        print("✅ Retrieved URLs:")
        print(json.dumps(urls, indent=2))
    except Exception as e:
        print("❌ Error fetching image URLs:", e)

# Run both steps
move_images_to_folder()
list_urls_in_folder()

# === WEBSITE ROUTES ===
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@route('/')
def index():
    return template('index')

@route('/category-sports')
def categorysports():
    return template('category-sports')

@route('/category-automotive')
def categoryautomotive():
    return template('category-automotive')

@route('/Training-15-05')
def Training1505():
    return template('Training-15-05')

@route('/Training-19-05')
def Training1905():
    return template('Training-19-05')

@route('/ChoirPractice11-06')
def ChoirPractice1106():
    return template('ChoirPractice11-06')

@route('/about')
def about():
    return template('about')

@route('/contact')
def contact():
    return template('contact')

@route('/googlec84cb0ca6911faab.html')
def googlec84cb0ca6911faab():
    return template('googlec84cb0ca6911faab.html')

@route('/sitemap.xml')
def sitemap():
    return template('sitemap.xml')

# Start server
if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)
