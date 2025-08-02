import os
import tempfile
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    Application,
)
from telegram import Update
from object_detection import ObjectDetection
from config import BOT_TOKEN, ADMIN_CHAT_ID, MODEL_PATH

# Initialize the YOLO object detection model
detector = ObjectDetection(model_path=MODEL_PATH)

async def send_startup_message(application: Application):
    """
    Sends a startup notification to the admin chat.
    """
    await application.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text="✅ Bot has started and is now monitoring!",
    )


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles the /start command.
    Sends a welcome message to the user with instructions.
    """
    await update.message.reply_text(
        f"👋 Welcome! {update.effective_user.full_name}\nSend me a photo and I'll detect objects in it."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles the /help command.
    Sends usage instructions and available commands to the user.
    """
    await update.message.reply_text(
        "ℹ️ I can detect objects in your images using AI!\n"
        "📸 Just send me a photo.\n"
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message"
    )


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles incoming photo messages.
    Processes the image to detect objects, annotates the image, and sends it back to the user.
    """
    input_path = None
    try:
        # Get the highest resolution version of the photo
        photo = update.message.photo[-1]
        file = await photo.get_file()

        await update.message.reply_text("📷 Received your image. Processing it now...")

        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_input:
            await file.download_to_drive(temp_input.name)
            input_path = temp_input.name

        # Perform detection
        detector.detect(input_path)
        summary = detector.detection_summary()
        image_stream = detector.get_image_stream()

        # Send result
        await update.message.reply_photo(photo=image_stream, caption=summary)

    except Exception as e:
        await update.message.reply_text(f"❌ Error during processing:\n{e}")

    finally:
        if input_path and os.path.exists(input_path):
            os.remove(input_path)


if __name__ == "__main__":
    # Create the bot application
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Set up startup notification
    app.post_init = send_startup_message

    # Add command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # Add photo handler
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    # Start the bot
    print("🤖 Bot Is Running...")
    app.run_polling()
