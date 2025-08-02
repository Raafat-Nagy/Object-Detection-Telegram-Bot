import io
import cv2
from ultralytics import YOLO


class ObjectDetection:
    """
    Class for handling object detection using YOLO.
    """

    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)
        self.results = None
        self.annotated_img = None

    def detect(self, image):
        """
        Perform object detection on the given image.

        Args:
            image (str or np.ndarray): Path to image or image array.

        Returns:
            np.ndarray: Annotated image with bounding boxes.
        """
        self.results = self.model(image)[0]
        self.annotated_img = self.results.plot()
        return self.annotated_img

    def detection_summary(self):
        """
        Generates a formatted detection summary from the last detection result.

        Returns:
            str: Summary string with image size, detected objects, and speed.
        """
        if self.results is None:
            return "⚠️ No detection results available."

        detected = self.results.verbose().strip()
        speed = self.results.speed
        shape = self.results.orig_shape

        message = "✅ Object Detection Completed!\n\n"
        message += f" • Size: {shape[0]}x{shape[1]}\n"
        message += f" • Objects: {detected}\n"
        message += (
            f" • Speed: {speed['preprocess']:.1f}ms preprocess, "
            f"{speed['inference']:.1f}ms inference, "
            f"{speed['postprocess']:.1f}ms postprocess"
        )
        return message

    def get_image_stream(self):
        """
        Encode the annotated image as a JPEG byte stream (for sending in Telegram, etc.).

        Returns:
            BytesIO: Encoded JPEG image as byte stream.
        """
        if self.annotated_img is None:
            return None

        _, encoded_image = cv2.imencode(".jpg", self.annotated_img)
        return io.BytesIO(encoded_image.tobytes())
