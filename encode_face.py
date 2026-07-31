import face_recognition
import pickle
import os

knownEncodings = []
knownNames = []

dataset_path = "dataset"

# Check dataset folder
if not os.path.exists(dataset_path):
    print("Dataset folder not found!")
    exit()

# Read all images
for filename in os.listdir(dataset_path):

    if filename.lower().endswith((".jpg", ".jpeg", ".png")):

        image_path = os.path.join(dataset_path, filename)

        print(f"Encoding {filename}...")

        image = face_recognition.load_image_file(image_path)

        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:

            knownEncodings.append(encodings[0])

            name = os.path.splitext(filename)[0]

            knownNames.append(name)

            print(f"✓ {name} encoded successfully")

        else:

            print(f"✗ No face found in {filename}")

# Save encodings
data = {
    "encodings": knownEncodings,
    "names": knownNames
}

with open("encodings.pickle", "wb") as f:
    pickle.dump(data, f)

print("\nEncodings saved successfully!")
print(f"Total faces encoded: {len(knownNames)}")