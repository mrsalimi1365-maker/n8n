class ColorCode:
    """
    کلاسی برای گرفتن نام رنگ و برگرداندن کد رنگ (Hex) متناظر با آن.
    """

    # دیکشنری نگاشت نام رنگ به کد Hex
    COLORS = {
        "red": "#FF0000",
        "green": "#00FF00",
        "blue": "#0000FF",
        "white": "#FFFFFF",
        "black": "#000000",
        "yellow": "#FFFF00",
        "cyan": "#00FFFF",
        "magenta": "#FF00FF",
        "gray": "#808080",
        "grey": "#808080",
        "orange": "#FFA500",
        "purple": "#800080",
        "pink": "#FFC0CB",
        "brown": "#A52A2A",
        "navy": "#000080",
        "lime": "#00FF00",
        "maroon": "#800000",
        "olive": "#808000",
        "teal": "#008080",
        "silver": "#C0C0C0",
        "gold": "#FFD700",
        "beige": "#F5F5DC",
        "turquoise": "#40E0D0",
        "violet": "#EE82EE",
        "indigo": "#4B0082",
    }

    def get_code(self, color_name: str) -> str:
        """
        نام رنگ را می‌گیرد و کد Hex متناظر با آن را برمی‌گرداند.
        اگر رنگ در لیست موجود نباشد، خطای ValueError می‌دهد.
        """
        if not isinstance(color_name, str):
            raise ValueError("نام رنگ باید یک رشته باشد.")

        key = color_name.strip().lower()
        if key not in self.COLORS:
            raise ValueError(f"رنگ '{color_name}' در لیست تعریف‌شده موجود نیست.")

        return self.COLORS[key]


def main():
    color_finder = ColorCode()
    name = input("نام رنگ را وارد کنید: ")
    try:
        code = color_finder.get_code(name)
        print(f"کد رنگ '{name}': {code}")
    except ValueError as e:
        print(f"خطا: {e}")


if __name__ == "__main__":
    main()
