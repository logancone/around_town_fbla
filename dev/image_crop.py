import os
from PIL import Image

# === CONFIG ===
image_folder = "raw_images"
output_folder = "new_images"
size = 512  # final thumbnail size

# Your business names IN ORDER matching the images
business_names = [
    "Harbor Roast Cafe",
    "Tidal Spoon Bistro",
    "Biscuit Bay Bakery",
    "Coastal Crumb Patisserie",
    "Salt And Smoke BBQ",
    "Pier 17 Deli",
    "Boardwalk Slice Pizza",
    "Dockside Dumplings",
    "Mango Moon Thai",
    "La Ola Taqueria",
    "Noodle Tide",
    "Green Fork Vegan Kitchen",
    "Sunrise Smoothies",
    "Blue Crab Seafood Shack",
    "Creamline Ice Cream",
    "Route 60 Burger House",
    "Corner Cafe",
    "Southside Sandwiches",
    "The Daily Brunch",
    "Bayberry Bistro",

    "Harbor Threads",
    "Seaside Sneakers",
    "TideTech",
    "Paper Moon Bookshop",
    "Market Basket Grocer",
    "QuickStop Convenience",
    "Willow Furnishings",
    "Home Harbor Goods",
    "Pearl & Pine Jewelry",
    "Shoreline Sporting Goods",
    "Coastal Thrift",
    "Pixel Point Electronics",
    "Outfit Outlet",
    "Lantern Housewares",
    "Wave Watchers Gear",
    "Bay Books & Gifts",
    "Dockside Decor",
    "Anchor Apparel",
    "Neon Nook Gaming Store",
    "Harbor Optical",

    "Neon Harbor Bowling",
    "Atomic Arcade",
    "Moonlight Cinema",
    "Tide Escape Rooms",
    "Seaside Mini Golf",
    "Harbor Stage Theatre",
    "Rhythm Room Karaoke",
    "LiveWire Music Hall",
    "Pixel Play Gaming Lounge",
    "Waves VR Arena",
    "Boardwalk Bounce",
    "Lighthouse Lanes",
    "Mariner's Magic Show",
    "Sunset Sports Center",
    "Harbor Haunt Nights",
    "Open Sky Amphitheater",
    "Coastline Comedy Club",
    "Bayfront Birthday Zone",
    "Dockside Event Hall",
    "Starlight Family Fun",

    "Clip & Clipper Barber Shop",
    "Fresh Fade Studio",
    "Spark Auto Repair",
    "Harbor Wash Car Care",
    "Nook Nail Studio",
    "Tide Pet Grooming",
    "Anchor Insurance",
    "Legal Harbor",
    "Ledger Financial",
    "Seaside Realty",
    "Bright Clean Services",
    "Pedal Pro Bike Repair",
    "Fit Harbor Gym",
    "Flow Yoga Studio",
    "Iron Tide Martial Arts",
    "Peak Personal Training",
    "Coastal Physical Therapy",
    "Wellness Bay Spa",
    "Brake & Tire Depot",
    "ByteFix Computer Repair"
]
# business_names = [
#     "logans lit bowling",
#     "freds food",
#     "johns jellies",
#     "billys barbershop",
#     "sarahs sweet treats",
#     "mikes bike repair",
#     "emmas art corner",
#     "chris retro arcade",
#     "olivias outdoor gear",
#     "daves detailing",
#     "lilys library lounge",
#     "noahs tech hub",
#     "zoes fitness studio"
# ]
os.makedirs(output_folder, exist_ok=True)

def safe_filename(name):
    # remove illegal filename characters
    return "".join(c for c in name if c.isalnum() or c in " _-").strip().replace(" ", "_")

def center_crop_square(img):
    width, height = img.size
    min_dim = min(width, height)

    left = (width - min_dim) // 2
    top = (height - min_dim) // 2
    right = left + min_dim
    bottom = top + min_dim

    return img.crop((left, top, right, bottom))

# get images sorted by filename (important since you said "downloaded in order")
images = [
    f for f in os.listdir(image_folder)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

# sort by creation time (download order on most systems)
images.sort(key=lambda f: os.path.getmtime(os.path.join(image_folder, f)), reverse=False)

if len(images) != len(business_names):
    raise ValueError(f"Mismatch: {len(images)} images vs {len(business_names)} businesses")

for img_file, business in zip(images, business_names):
    img_path = os.path.join(image_folder, img_file)

    with Image.open(img_path) as img:
        img = img.convert("RGB")

        # crop center square
        img = center_crop_square(img)

        # resize down
        img = img.resize((size, size), Image.Resampling.LANCZOS)

        # save
        filename = safe_filename(business.lower()) + ".jpg"
        save_path = os.path.join(output_folder, filename)

        img.save(save_path, quality=90)

print("Done processing images.")