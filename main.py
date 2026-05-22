import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import os
from pathlib import Path
import threading
import sys

SCRIPT_DIR = Path(__file__).parent.absolute()


class CCConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CCAssistant")
        self.root.geometry("600x700")

        # Create notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create tabs
        self.image_tab = ttk.Frame(self.notebook)
        self.audio_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.image_tab, text="Image to NFP")
        self.notebook.add(self.audio_tab, text="Audio/Video to DFPWM")

        self.setup_image_tab()
        self.setup_audio_tab()

        # Status bar
        self.status_frame = ttk.Frame(root)
        self.status_frame.pack(fill=tk.X, padx=10, pady=5)
        self.status_label = ttk.Label(self.status_frame, text="Ready", relief=tk.SUNKEN)
        self.status_label.pack(fill=tk.X)

    def setup_image_tab(self):
        frame = ttk.LabelFrame(self.image_tab, text="Image Conversion Settings", padding=15)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # File selection
        file_frame = ttk.Frame(frame)
        file_frame.pack(fill=tk.X, pady=10)
        ttk.Label(file_frame, text="Image File:").pack(side=tk.LEFT)
        self.image_path = tk.StringVar()
        ttk.Entry(file_frame, textvariable=self.image_path, state="readonly", width=40).pack(side=tk.LEFT, padx=5)
        ttk.Button(file_frame, text="Browse", command=self.select_image_file).pack(side=tk.LEFT)

        # Monitor width
        width_frame = ttk.Frame(frame)
        width_frame.pack(fill=tk.X, pady=5)
        ttk.Label(width_frame, text="Monitor Width:", width=15).pack(side=tk.LEFT)
        self.monitor_width = tk.StringVar(value="3")
        ttk.Spinbox(width_frame, from_=1, to=10, textvariable=self.monitor_width, width=10).pack(side=tk.LEFT, padx=5)
        ttk.Label(width_frame, text="(number of monitors)").pack(side=tk.LEFT)

        # Monitor height
        height_frame = ttk.Frame(frame)
        height_frame.pack(fill=tk.X, pady=5)
        ttk.Label(height_frame, text="Monitor Height:", width=15).pack(side=tk.LEFT)
        self.monitor_height = tk.StringVar(value="3")
        ttk.Spinbox(height_frame, from_=1, to=10, textvariable=self.monitor_height, width=10).pack(side=tk.LEFT, padx=5)
        ttk.Label(height_frame, text="(number of monitors)").pack(side=tk.LEFT)

        # Text scale
        scale_frame = ttk.Frame(frame)
        scale_frame.pack(fill=tk.X, pady=5)
        ttk.Label(scale_frame, text="Text Scale:", width=15).pack(side=tk.LEFT)
        self.text_scale = tk.StringVar(value="0.5")
        ttk.Spinbox(scale_frame, from_=0.1, to=5.0, increment=0.1, textvariable=self.text_scale, width=10).pack(side=tk.LEFT, padx=5)
        ttk.Label(scale_frame, text="(text size multiplier)").pack(side=tk.LEFT)

        # Display calculated dimensions
        calc_frame = ttk.LabelFrame(frame, text="Calculated Dimensions", padding=10)
        calc_frame.pack(fill=tk.X, pady=15)

        self.calc_label = ttk.Label(calc_frame, text="Resize Width: 0 | Resize Height: 0", font=("Arial", 10))
        self.calc_label.pack()

        # Bind changes to update calculations
        self.monitor_width.trace("w", self.update_calculations)
        self.monitor_height.trace("w", self.update_calculations)
        self.text_scale.trace("w", self.update_calculations)

        # Convert button
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, pady=15)
        ttk.Button(button_frame, text="Convert to NFP", command=self.convert_image).pack(side=tk.LEFT, padx=5)

    def setup_audio_tab(self):
        frame = ttk.LabelFrame(self.audio_tab, text="Audio/Video Conversion Settings", padding=15)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # File selection
        file_frame = ttk.Frame(frame)
        file_frame.pack(fill=tk.X, pady=10)
        ttk.Label(file_frame, text="Audio/Video File:").pack(side=tk.LEFT)
        self.audio_path = tk.StringVar()
        ttk.Entry(file_frame, textvariable=self.audio_path, state="readonly", width=40).pack(side=tk.LEFT, padx=5)
        ttk.Button(file_frame, text="Browse", command=self.select_audio_file).pack(side=tk.LEFT)

        # Info
        info_frame = ttk.LabelFrame(frame, text="Supported Formats", padding=10)
        info_frame.pack(fill=tk.X, pady=15)
        ttk.Label(info_frame, text="Audio: MP3, WAV, OGG, FLAC, M4A, etc.\nVideo: MP4, MKV, AVI, MOV, WebM, etc.").pack()

        # Convert button
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, pady=15)
        ttk.Button(button_frame, text="Convert to DFPWM", command=self.convert_audio).pack(side=tk.LEFT, padx=5)

    def update_calculations(self, *args):
        try:
            width = int(self.monitor_width.get())
            height = int(self.monitor_height.get())
            scale = float(self.text_scale.get())

            # Calculate characters using correct formula from monitorsize calculator
            resize_width = round((64 * width - 20) / (6 * scale))
            resize_height = round((64 * height - 20) / (9 * scale))

            self.calc_label.config(text=f"Resize Width: {resize_width} | Resize Height: {resize_height}")
        except (ValueError, ZeroDivisionError):
            self.calc_label.config(text="Resize Width: -- | Resize Height: --")

    def select_image_file(self):
        file = filedialog.askopenfilename(
            title="Select Image File",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif"), ("All Files", "*.*")]
        )
        if file:
            self.image_path.set(file)

    def select_audio_file(self):
        file = filedialog.askopenfilename(
            title="Select Audio/Video File",
            filetypes=[
                ("Common Formats", "*.mp3 *.mp4 *.wav *.mkv *.avi *.mov *.webm *.m4a *.ogg *.flac"),
                ("All Files", "*.*")
            ]
        )
        if file:
            self.audio_path.set(file)

    def update_status(self, message):
        self.status_label.config(text=message)
        self.root.update()

    def convert_image(self):
        if not self.image_path.get():
            messagebox.showerror("Error", "Please select an image file")
            return

        try:
            width = int(self.monitor_width.get())
            height = int(self.monitor_height.get())
            scale = float(self.text_scale.get())

            # Calculate characters using correct formula from monitorsize calculator
            resize_width = round((64 * width - 20) / (6 * scale))
            resize_height = round((64 * height - 20) / (9 * scale))

            input_path = self.image_path.get()
            output_path = str(Path(input_path).with_suffix(".nfp"))

            self.update_status(f"Converting image: {Path(input_path).name}")

            # Run conversion in background thread
            thread = threading.Thread(
                target=self._run_image_conversion,
                args=(input_path, output_path, resize_width, resize_height)
            )
            thread.daemon = True
            thread.start()

        except ValueError:
            messagebox.showerror("Error", "Invalid parameter values")

    def _run_image_conversion(self, input_path, output_path, width, height):
        try:
            convert_nfp_path = SCRIPT_DIR / "converters" / "convert_nfp.py"
            cmd = [
                sys.executable,
                str(convert_nfp_path),
                input_path,
                f"--resize-width={width}",
                f"--resize-height={height}"
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, check=True, cwd=str(SCRIPT_DIR))
            self.update_status(f"✓ Image converted: {Path(output_path).name}")
            messagebox.showinfo("Success", f"Image converted to:\n{output_path}")
        except subprocess.CalledProcessError as e:
            self.update_status("✗ Conversion failed")
            messagebox.showerror("Conversion Error", f"Error:\n{e.stderr}")
        except Exception as e:
            self.update_status("✗ Error occurred")
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

    def convert_audio(self):
        if not self.audio_path.get():
            messagebox.showerror("Error", "Please select an audio/video file")
            return

        input_path = self.audio_path.get()
        output_path = str(Path(input_path).with_suffix(".dfpwm"))

        self.update_status(f"Converting audio: {Path(input_path).name}")

        # Run conversion in background thread
        thread = threading.Thread(
            target=self._run_audio_conversion,
            args=(input_path, output_path)
        )
        thread.daemon = True
        thread.start()

    def _run_audio_conversion(self, input_path, output_path):
        try:
            # Use ffmpeg to convert to DFPWM
            cmd = [
                "ffmpeg",
                "-i", input_path,
                # "-af", "aformat=s8:8000",
                "-c:a", "dfpwm",
                output_path,
                "-y"  # Overwrite output file
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            self.update_status(f"✓ Audio converted: {Path(output_path).name}")
            messagebox.showinfo("Success", f"Audio converted to:\n{output_path}")
        except subprocess.CalledProcessError as e:
            self.update_status("✗ Conversion failed")
            messagebox.showerror("Conversion Error", f"FFmpeg error:\n{e.stderr}")
        except FileNotFoundError:
            self.update_status("✗ ffmpeg not found")
            messagebox.showerror("Error", "ffmpeg not found. Make sure it's installed and in your PATH.")
        except Exception as e:
            self.update_status("✗ Error occurred")
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CCConverterGUI(root)
    root.mainloop()
