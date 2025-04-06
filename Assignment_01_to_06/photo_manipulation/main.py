from PIL import Image, ImageEnhance, ImageFilter
import sys

# Open an image file
def open_image(image_path):
    try:
        image = Image.open(image_path)
        print(f"Image '{image_path}' opened successfully!")
        return image
    except Exception as e:
        print(f"Error opening image: {e}")
        sys.exit(1)

# Adjust brightness of the image
def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

# Adjust contrast of the image
def adjust_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

# Apply blur filter to the image
def apply_blur(image, radius=2):
    return image.filter(ImageFilter.GaussianBlur(radius))

# Save the image
def save_image(image, output_path):
    try:
        image.save(output_path)
        print(f"Image saved as {output_path}")
    except Exception as e:
        print(f"Error saving image: {e}")

# Main function
def main():
    input_image_path = input("Enter the path of the image you want to manipulate: ")
    image = open_image(input_image_path)

    # Adjust brightness
    brightness_factor = float(input("Enter brightness factor (1.0 = original, >1.0 = brighter): "))
    image = adjust_brightness(image, brightness_factor)

    # Adjust contrast
    contrast_factor = float(input("Enter contrast factor (1.0 = original, >1.0 = more contrast): "))
    image = adjust_contrast(image, contrast_factor)

    # Apply blur
    apply_blur_choice = input("Do you want to apply a blur effect? (yes/no): ").strip().lower()
    if apply_blur_choice == 'yes':
        blur_radius = float(input("Enter the blur radius (e.g., 2): "))
        image = apply_blur(image, blur_radius)

    # Save the manipulated image
    output_image_path = input("Enter the path to save the manipulated image: ")
    save_image(image, output_image_path)

if __name__ == "__main__":
    main()
