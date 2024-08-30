try:
    import qrcode, argparse, random, string, sys, logging
    from PIL import Image, ImageDraw
except (ModuleNotFoundError) as e:
    __import__("sys").exit(f"[Error] {str(e).capitalize()}!")

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

def generate_random_link():
    code_length = 9  # CHANGE THE LENGTH OF THE LINK AS YOU WISH!
    random_code = "".join(
        random.choice(string.ascii_lowercase + string.digits)
        for _ in range(code_length)
    )
    random_link = "https://link.dana.id/kaget?c=" + random_code
    return random_link

def generate_image(path, link, image):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)

    img_qr = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

    logo = Image.open(f"Logo/Dana-{image}.png")

    img_qr_w, img_qr_h = img_qr.size
    logo_size = min(img_qr_w, img_qr_h) // 4

    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    transparent = Image.new("RGBA", (img_qr_w, img_qr_h), (0, 0, 0, 0))
    transparent.paste(img_qr, (0, 0))

    transparent.paste(
        logo, ((img_qr_w - logo_size) // 2, (img_qr_h - logo_size) // 2), logo
    )

    mask = Image.new("L", (img_qr_w, img_qr_h), 0)
    draw = ImageDraw.Draw(mask)
    radius = 27  # YOU CAN ADJUST THE BLUNT ANGLE!
    draw.rounded_rectangle([0, 0, img_qr_w, img_qr_h], radius=radius, fill=255)

    rounded_qr = Image.new("RGBA", (img_qr_w, img_qr_h))
    rounded_qr.paste(transparent, (0, 0), mask=mask)

    rounded_qr.save(
        f"{path}{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}.png"
    )

def main(path, link, count, image):
    try:
        count = 1 if link != "null" and count >= 1 else count
        link = generate_random_link() if link == "null" else link
        path = path.rstrip("/") + "/"
        image = image if image in [1, 2, 3, 4] else 1

        logging.info(f"Directory: {path}")
        logging.info(f"Tutan: {link}")
        logging.info(f"Count: {count}")
        logging.info(f"Using image number: {image} for the logo\n")

        for i in range(count):
            logging.info(f"Memproses QR ke-{i + 1} untuk link: {link}...")
            generate_image(path, link, image)
        sys.exit(1)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(
            description="Program ini menerima path untuk direktori penyimpanan, sebuah link, jumlah iterasi, dan pilihan gambar, kemudian memproses link tersebut sebanyak jumlah iterasi yang diminta."
        )

        parser.add_argument(
            "COUNT", type=int, help="Jumlah iterasi untuk memproses link tersebut."
        )
        parser.add_argument(
            "PATH", type=str, help="Direktori di mana file gambar akan disimpan."
        )
        parser.add_argument(
            "IMAGE",
            type=int,
            help="Nomor gambar yang akan digunakan sebagai logo (1, 2, 3, atau 4).",
        )
        parser.add_argument(
            "LINK", type=str, help="Link yang akan diproses oleh program."
        )

        args = parser.parse_args()

        main(args.PATH, args.LINK, args.COUNT, args.IMAGE)
    except Exception as e:
        logging.critical(f"Failed to start the program: {e}")
        sys.exit(1)