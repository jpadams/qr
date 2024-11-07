"""A module with qr code functions"""

import qrcode
import qrcode.image.pil
import dagger
from dagger import function, object_type

@object_type
class Qr:
    @function
    def generate_ascii_qr(self, data: str) -> str:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=1,
            border=1,
        )
        qr.add_data(data)
        qr.make(fit=True)
    
        qr_matrix = qr.get_matrix()
        ascii_art = ""
    
        for row in qr_matrix:
            for cell in row:
                ascii_art += "██" if cell else "  "
            ascii_art += "\n"
    
        return ascii_art
