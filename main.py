from database import create_tables
from services import *
from PySide6.QtWidgets import QApplication
from gui import LoginPage, DiscoverPage, MainWindow

from uic_conversion import convert_ui_to_py

def fill_with_fake_data():
    # Users
    add_user("logan", "password")
    add_user("fred", "password")
    add_user("john", "password")
    add_user("billy", "password")
    add_user("sarah", "password")
    add_user("mike", "password")
    add_user("emma", "password")
    add_user("chris", "password")
    add_user("olivia", "password")
    add_user("q", "q")

    # Businesses
    add_business(
        "Billy's Barbershop",
        4,
        "Services",
        "images/billys_barbershop.jpg",
        "A great, friendly place to get a haircut. I've been cutting hair for over 30 years and I love talking with customers while I work. We do classic cuts, fades, and beard trims. Come on Tuesdays for 10% off any service."
    )

    add_business(
        "Logan's Lit Bowling",
        1,
        "Entertainment",
        "images/logans_lit_bowling.jpg",
        "A modern bowling alley with music, lights, and late-night games. Great for hanging out with friends or hosting casual competitions. Use code STRIKE20 for 20% off lane reservations on weekends."
    )

    add_business(
        "John's Jellies",
        3,
        "Retail",
        "images/johns_jellies.jpg",
        "Small-batch homemade jellies and fruit spreads made with real ingredients. I started making these for friends and it slowly turned into a small business. There are always a few weird experimental flavors available if you're feeling adventurous."
    )

    add_business(
        "Fred's Food",
        2,
        "Food",
        "images/freds_food.png",
        "Local comfort food made fresh every day. Burgers, sandwiches, and homemade sides are the staples here. It's not fancy, but it’s consistent and filling."
    )

    add_business(
        "Sarah's Sweet Treats",
        5,
        "Food",
        "images/sarahs_sweet_treats.jpg",
        "A cozy little bakery focused on cookies, brownies, and cupcakes. Everything is baked the same morning it’s sold. Stop by on Fridays for a buy‑one‑get‑one cupcake deal."
    )

    add_business(
        "Mike's Bike Repair",
        6,
        "Services",
        "images/mikes_bike_repair.jpg",
        "Neighborhood bike repair shop that handles everything from flat tires to full rebuilds. I try to keep prices fair and turnaround fast. Cyclists of all skill levels are welcome. If you mention this listing you’ll get a free brake adjustment with any repair."
    )

    add_business(
        "Emma's Art Corner",
        7,
        "Retail",
        "images/emmas_art_corner.jpg",
        "Small art shop selling prints, stickers, and handmade crafts from local artists. The goal is to give creative people a place to show their work. Inventory changes a lot so there’s usually something new every week."
    )

    add_business(
        "Chris's Retro Arcade",
        8,
        "Entertainment",
        "images/chris_retro_arcade.jpg",
        "An arcade filled with classic machines from the 80s and 90s. Pinball, fighting games, racing cabinets, and a few rare finds. It’s loud, nostalgic, and meant to feel like old school gaming again."
    )

    add_business(
        "Olivia's Outdoor Gear",
        9,
        "Retail",
        "images/olivias_outdoor_gear.jpg",
        "Outdoor equipment for hiking, camping, and beginner adventurers. I focus on durable gear that isn't ridiculously overpriced. Staff are happy to help new hikers figure out what they actually need."
    )

    # Reviews

    # Business 1 - Billy's Barbershop
    add_review(1, 1, 5, "Billy absolutely knows what he's doing. Best haircut I've had in years.")
    add_review(2, 1, 4.5, "Great atmosphere and conversation. Cut was solid.")
    add_review(3, 1, 3, "Decent haircut but had to wait a long time.")
    add_review(5, 1, 4, "Friendly guy and good prices.")
    add_review(6, 1, 2.5, "Not terrible but the style wasn't exactly what I asked for.")
    add_review(7, 1, 5, "Perfect fade. I'll definitely be back.")
    add_review(8, 1, 4, "Old school barber vibe which I liked.")

    # Business 2 - Logan's Lit Bowling
    add_review(2, 2, 4.5, "Fun place with friends. The lights and music make it way better than normal bowling.")
    add_review(3, 2, 4, "Pretty cool but lanes were a little crowded.")
    add_review(4, 2, 5, "Had a birthday here and it was awesome.")
    add_review(5, 2, 3, "It's okay. Just bowling with louder music.")
    add_review(6, 2, 4, "Staff were nice and everything worked.")
    add_review(7, 2, 2.5, "Shoes were kinda worn out.")

    # Business 3 - John's Jellies
    add_review(1, 3, 4.5, "Actually really good. The strawberry one was amazing.")
    add_review(2, 3, 3.5, "Some flavors are great, some are weird.")
    add_review(4, 3, 5, "Bought a few jars and finished them way too fast.")
    add_review(5, 3, 4, "Good local product.")
    add_review(6, 3, 2, "Not really my thing.")
    add_review(7, 3, 4.5, "Unique flavors and nice packaging.")

    # Business 4 - Fred's Food
    add_review(1, 4, 4, "Solid burger and fries.")
    add_review(3, 4, 3, "Food was decent but nothing special.")
    add_review(4, 4, 4.5, "Really liked the sandwiches.")
    add_review(5, 4, 2.5, "Service was slow when I went.")
    add_review(6, 4, 5, "Great comfort food.")
    add_review(7, 4, 3.5, "Good portion sizes.")
    add_review(8, 4, 4, "Nice casual spot.")

    # Business 5 - Sarah's Sweet Treats
    add_review(1, 5, 5, "Cupcakes were incredible.")
    add_review(2, 5, 4, "Really good desserts but a bit sweet.")
    add_review(3, 5, 3.5, "Pretty good bakery.")
    add_review(4, 5, 4.5, "Cookies were fantastic.")

    # Business 6 - Mike's Bike Repair
    add_review(1, 6, 4.5, "Fixed my bike way faster than I expected.")
    add_review(2, 6, 5, "Super helpful and explained everything.")
    add_review(3, 6, 3.5, "Good work but a little pricey.")
    add_review(4, 6, 4, "Solid repair shop.")
    add_review(5, 6, 4.5, "Bike rides like new.")

    # Business 7 - Emma's Art Corner
    add_review(1, 7, 4, "Cute shop with interesting stuff.")
    add_review(2, 7, 4.5, "Found some really cool prints.")
    add_review(3, 7, 3, "Nice but small.")
    add_review(4, 7, 5, "Loved supporting local artists.")
    add_review(5, 7, 4, "Good variety.")
    add_review(6, 7, 2.5, "A bit pricey.")

    # Business 8 - Chris's Retro Arcade
    add_review(1, 8, 5, "This place is awesome.")
    add_review(2, 8, 4.5, "Great selection of games.")
    add_review(3, 8, 3.5, "Fun but kinda loud.")
    add_review(4, 8, 4, "Brought back memories.")
    add_review(5, 8, 2.5, "Some machines were broken.")

    # Business 9 - Olivia's Outdoor Gear
    add_review(1, 9, 4, "Helpful staff.")
    add_review(2, 9, 3.5, "Decent gear selection.")
    add_review(3, 9, 5, "Got everything I needed for a hiking trip.")
    add_review(4, 9, 4.5, "Good quality stuff.")
    add_review(5, 9, 3, "Prices are okay.")
    add_review(6, 9, 4, "Nice small outdoor shop.")

    # toggle_bookmark(1, 1)
    # toggle_bookmark(1, 4)
    # toggle_bookmark(1, 3)
    # toggle_bookmark(1, 6)
    # toggle_bookmark(1, 8)


def gui_init():
    app = QApplication()
    with open("style.qss", "r", encoding='utf-8') as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    app.exec()

def main():
    create_tables()
    fill_with_fake_data()

    gui_init()

if __name__ == "__main__":
    # convert_ui_to_py() #Remove for presentation!
    main()