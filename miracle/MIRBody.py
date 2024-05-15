"""
A representation of the .MIR body
"""

class MIRBody:
    def __init__(self) -> None:
        self.passanger_section: list[dict] = []
        self.fare_section: list[dict] = []
        self.fare_basis: list[dict] = []
        self.rail_section: list[dict] = []

    def parse(self, data: bytes):
        sections: list[bytes] = data.split(b"\r")
        sections.remove(b"")  # Remove empty

        # Iterate over the sections to parse
        for section in sections:
            subsection: str = section.decode("utf-8")
            section_code = subsection[0:3]

            match section_code:
                case "A02":
                    # Append data to data sections
                    section_data = {
                        "passenger_name": subsection[3:33].strip(),
                        "transaction_number": subsection[36:47],
                    }

                    self.passanger_section.append(section_data)

                    continue

                case "A04":
                    section_data = {
                        "departure_date": subsection[30:35],
                        "departure_time": subsection[35:40],
                        "arrival_time": subsection[40:45],
                        "arival_factor": subsection[45:46],
                        "origin": {
                            "city_code": subsection[46:49].strip(),
                            "city_name": subsection[49:62].strip(),
                        },
                        "destination": {
                            "city_code": subsection[62:65].strip(),
                            "city_name": subsection[65:78].strip(),
                        },
                        "flight_type": subsection[78:79].strip(),
                        "number_of_stops": int(subsection[85:86]),
                    }
                    self.rail_section.append(section_data)
                    continue

                case "A07":
                    section_data = {
                        "currency_code": subsection[5:8],
                        "base_fare_amount": float(subsection[8:20]),
                        "currency_code_for_total": subsection[20:23],
                        "total_amount": float(subsection[23:35].strip()),
                        "equivalent_amount_currency_code": subsection[35:38].strip(),
                        "equivalent_amount": float(subsection[38:50].strip()),
                    }
                    self.fare_section.append(section_data)
                    continue

                case "A08":
                    section_data = {
                        "fare_basis_code": subsection[7:15].strip(),
                        "not_valid_before": subsection[23:30].strip(),
                        "not_valid_after": subsection[30:37].strip(),
                    }
                    self.fare_basis.append(section_data)
                    continue

                case _:
                    continue

    def to_serializable(self) -> dict:
        return {
            "passenger_section": self.passanger_section,
            "fare_section": self.fare_section,
            "fare_basis": self.fare_basis,
            "rail_section": self.rail_section,
        }
