"""
MIRHeader

Author: Erick Muuo
A class representing the header of the .MIR file format
"""

from datetime import datetime


class MIRHeader:
    def __init__(self, file_path: str = "") -> None:
        self.file_path: str = file_path
        self.header_info: dict = {}

    def from_bytes(self, data: bytes) -> bool | None:
        """
        Parses the header from the given bytes and stores the information.

        Args:
            data (bytes): The byte data representing the header.

        Returns:
            bool: True if parsing was successful, False otherwise.

        Exceptions:
            May throw an exception incase the data is not parsable
        """
        try:
            # Example parsing logic
            if len(data) < 343:  # Assume the header must be at least 10 bytes
                raise Exception(
                    "The bytes provided were less than the expected 343 bytes of the header section"
                )

            self.header_info = {
                "basic_id": data[0:2].decode("utf-8"),
                "transmitting_system": data[2:4].decode("utf-8"),
                "iata": data[4:8].decode("utf-8"),  # Example field 3
                "mir_type_indicator": int(data[8:10].decode("utf-8")),
                "record_size": int(data[10:15].decode("utf-8")),
                "sequence_number": int(data[15:20].decode("utf-8")),
                "creation_date": data[20:27].decode("utf-8"),
                "creation_time": data[27:32].decode("utf-8"),
                "airline_date": {
                    "airline_code": data[32:34].decode("utf-8"),
                    "airline_number": data[34:37].decode("utf-8"),
                    "airline_name": data[37:61].decode("utf-8").strip(),
                },
                "date_of_first_travel": data[61:68].decode("utf-8").strip(),
                "booking_agency_account_code": data[81:85].decode("utf-8").strip(),
                "issuing_agency_account_code": data[85:89].decode("utf-8").strip(),
                "agency_account_number": data[89:98].decode("utf-8").strip(),
                "record_locator": data[98:104].decode("utf-8").strip(),
                "record_locator_from_originating": data[104:110]
                .decode("utf-8")
                .strip(),
                "other_airline_code": data[110:112].decode("utf-8"),
                "booking_agent_sign": data[113:119].decode("utf-8"),
                "ticketing_agent_sign": data[120:122].decode("utf-8"),
                "currency_code": data[145:148].decode("utf-8"),
                "decimal_places_in_currency": int(data[160:161].decode("utf-8")),
                "currency_code_for_tax_and_commission": data[161:164].decode("utf8"),
            }
            return True
        except Exception as e:
            # Handle parsing exceptions
            print(f"Failed to parse header: {e}")
            return False

    def __str__(self):
        return f"MIRHeader(file_path={self.file_path}, header_info={self.header_info})"
