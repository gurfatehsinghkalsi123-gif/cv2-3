import cv2

def annotate_image_width(image_path, output_path):
    image = cv2.imread(image_path)

    height, width, _ = image.shape

    start_point = (0, height // 2)
    end_point = (width, height // 2)

    cv2.arrowedLine(image, start_point, end_point, (0, 255, 0), 3, tipLength=0.05)
    cv2.arrowedLine(image, end_point, start_point, (0, 255, 0), 3, tipLength=0.05)

    text = f"Width: {width} pixels"
    text_position = (width // 4, height // 2 - 20)

    cv2.putText(image, text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imwrite(output_path, image)
    print("Width annotation completed successfully")

def main():
    input_image = "win.jpg"
    output_image = "output_annotated.jpg"
    annotate_image_width(input_image, output_image)

if __name__ == "__main__":
    main()