def main():
    age = int(input("ENTER YOUR CURRENT AGE: "))
    id_proof = input("ID AVAILABILITY ENTER yes OR no: ").lower()
    movie_rating = input("ENTER MOVIE RATING (U/UA/A): ").upper()
    is_member = input("ARE YOU A MEMBER ENTER yes OR no: ").lower()
    seats_available = int(input("ENTER THE AVAILABLE SEATS: "))
    seats_requested = int(input("ENTER THE REQUIRED SEATS: "))

    eligible = False

    # Seat availability check
    if seats_requested <= 0:
        print("❌ Seats requested must be greater than 0.")

    elif seats_requested > seats_available:
        print("❌ Not enough seats available.")

    else:
        # Age + rating check
        if movie_rating == "A":
            if age < 18:
                print("❌ Not eligible: A-rated, must be 18+.")
            elif id_proof == "no":
                print("❌ ID required for A-rated movies.")
            else:
                eligible = True

        elif movie_rating == "UA":
            if age >= 12:
                eligible = True
            else:
                parental_consent = input("PARENTAL CONSENT (yes/no): ").lower()

                if parental_consent == "yes":
                    eligible = True
                else:
                    print("❌ Parental consent required for UA-rated movies.")

        elif movie_rating == "U":
            eligible = True

        else:
            print("❌ Invalid movie rating.")

        # Pricing: only runs if all checks passed
        if eligible:
            price = 200

            if is_member == "yes" and seats_requested >= 2:
                price_per_ticket = price * 0.85
                discount = "15% member discount"

            elif is_member == "yes":
                price_per_ticket = price * 0.90
                discount = "10% member discount"

            elif seats_requested >= 4:
                price_per_ticket = price * 0.95
                discount = "5% bulk discount"

            else:
                price_per_ticket = price
                discount = "No discount"

            total = price_per_ticket * seats_requested

            print("\n✅ Booking Confirmed")
            print(f"Price per ticket: ₹{price_per_ticket:.1f} ({discount})")
            print(f"Total: ₹{total:.1f}")


main()
