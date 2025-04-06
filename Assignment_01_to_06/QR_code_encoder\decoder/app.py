import qrcode
import cv2
from pyzbar.pyzbar import decode
import os

# Generate QR code and save as image
def generate_qr(data, filename="myqrcode.png"):
    qr = qrcode.make(data)
    qr.save(filename)
    print(f"✅ QR code saved as {filename}")

# Decode QR from an image
def decode_qr_from_image(filename):
    img = cv2.imread(filename)
    decoded_objects = decode(img)

    for obj in decoded_objects:
        print("🧾 Data found:", obj.data.decode("utf-8"))

# Decode QR using webcam
def decode_qr_from_webcam():
    cap = cv2.VideoCapture(0)
    print("📸 Scanning... Press 'q' to quit.")
    
    while True:
        _, frame = cap.read()
        decoded_objects = decode(frame)

        for obj in decoded_objects:
            data = obj.data.decode('utf-8')
            print("📤 QR Code Data:", data)
            cv2.putText(frame, data, (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Main menu
def main():
    while True:
        print("\n=== QR Code Project ===")
        print("1. Generate QR Code")
        print("2. Decode QR Code from Image")
        print("3. Decode QR Code from Webcam")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            data = input("Enter the data to encode: ")
            filename = input("Enter filename to save (e.g. code.png): ")
            generate_qr(data, filename)
        elif choice == "2":
            filename = input("Enter image filename (e.g. code.png): ")
            if os.path.exists(filename):
                decode_qr_from_image(filename)
            else:
                print("❌ File not found.")
        elif choice == "3":
            decode_qr_from_webcam()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
