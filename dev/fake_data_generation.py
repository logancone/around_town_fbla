import random
from services.user_services import add_user
from services.business_services import add_business, add_review, add_preset_tag, set_business_tag

sample_usernames = [
 'logan',
 'fred',
 'john',
 'billy',
 'sarah',
 'mike',
 'emma',
 'chris',
 'olivia',
 'dave',
 'lily',
 'noah',
 'zoe',
 'alex',
 'ava',
 'brandon',
 'brooke',
 'caleb',
 'cameron',
 'carter',
 'chelsea',
 'claire',
 'colin',
 'courtney',
 'dakota',
 'elena',
 'evelyn',
 'gabriel',
 'grace',
 'hannah',
 'harper',
 'ian',
 'isabel',
 'jacob',
 'jasmine',
 'jordan',
 'kendra',
 'leah',
 'luca',
 'madison',
 'mason',
 'mia',
 'nathan',
 'nora',
 'owen',
 'paige',
 'quinn',
 'reagan',
 'reese',
 'ryan',
 'sadie',
 'samuel',
 'samantha',
 'scarlett',
 'sebastian',
 'stella',
 'talia',
 'theo',
 'tristan',
 'victoria',
 'violet',
 'wyatt',
 'zach',
 'adrian',
 'alina',
 'bianca',
 'blake',
 'brooklyn',
 'caroline',
 'damian',
 'dylan',
 'ella',
 'ethan',
 'faith',
 'felix',
 'gianna',
 'hazel',
 'hunter',
 'iris',
 'jules',
 'kevin',
 'lena',
 'lucas',
 'madeline',
 'marcus',
 'naomi',
 'noelle',
 'oliver',
 'parker',
 'riley',
 'sienna',
 'tyler',
 'zoey']

sample_businesses = [
  {'title': "Logan's Lit Bowling",
    'category': 'entertainment',
    'thumbnail': 'resources/images/business_thumbnails/logans_lit_bowling.jpg',
    'description': "A modern bowling alley with music, lights, and late-night games. "
                "Great for hanging out with friends or hosting casual competitions. Use code STRIKE20 for "
                "20% off lane reservations on weekends.",
    'lat': 37.083912,
    'lon': -76.478554,
    'tags': [18, 79, 80, 82]},
  {'title': "Fred's Food",
    'category': 'food',
    'thumbnail': 'resources/images/business_thumbnails/freds_food.jpg',
    'description': "Local comfort food made fresh every day. Burgers, sandwiches, and homemade sides are "
                "the staples here. It's not fancy, but it's consistent and filling. Combo meals are 15% off "
                "after 5 PM.",
    'lat': 37.089321,
    'lon': -76.512114,
    'tags': [1, 8, 86, 93]},
  {'title': "John's Jellies",
    'category': 'retail',
    'thumbnail': 'resources/images/business_thumbnails/johns_jellies.jpg',
    'description': "Small-batch homemade jellies and fruit spreads made with real ingredients. I started making "
                "these for friends and it slowly turned into a small business. There are always a few weird experimental "
                "flavors available if you're feeling adventurous. Use code SWEET10 for 10% off your first order.",
    'lat': 37.061744,
    'lon': -76.507829,
    'tags': [34, 88, 95]},
  {'title': "Billy's Barbershop",
    'category': 'services',
    'thumbnail': 'resources/images/business_thumbnails/billys_barbershop.jpg',
    'description': "A great, friendly place to get a haircut. I've been cutting hair for over 30 years and I love "
                "talking with customers while I work. We do classic cuts, fades, and beard trims. Come on Tuesdays "
                "for 10% off any service.",
    'lat': 37.072465,
    'lon': -76.493371,
    'tags': [58, 85, 88]},
  {'title': "Sarah's Sweet Treats",
    'category': 'food',
    'thumbnail': 'resources/images/business_thumbnails/sarahs_sweet_treats.jpg',
    'description': "A cozy little bakery focused on cookies, brownies, and cupcakes. Everything is baked the same morning it's "
                "sold. Stop by on Fridays for a buy-one-get-one cupcake deal.",
    'lat': 37.058932,
    'lon': -76.482667,
    'tags': [5, 6, 79, 88]  },
  {'title': "Mike's Bike Repair",
    'category': 'services',
    'thumbnail': 'resources/images/business_thumbnails/mikes_bike_repair.jpg',
    'description': "Neighborhood bike repair shop that handles everything from flat tires to full rebuilds. I try to "
                "keep prices fair and turnaround fast. Cyclists of all skill levels are welcome. If you mention this listing "
                "you'll get a free brake adjustment with any repair.",
    'lat': 37.094188,
    'lon': -76.501923,
    'tags': [39, 88, 95]},
  {'title': "Emma's Art Corner",
    'category': 'retail',
    'thumbnail': 'resources/images/business_thumbnails/emmas_art_corner.jpg',
    'description': "Small art shop selling prints, stickers, and handmade crafts from local artists. "
                "The goal is to give creative people a place to show their work. Inventory changes a lot so there's "
                "usually something new every week. Students get 10% off with ID.",
    'lat': 37.067744,
    'lon': -76.469882,
    'tags': [53, 88, 79]},
  {'title': "Chris's Retro Arcade",
    'category': 'entertainment',
    'thumbnail': 'resources/images/business_thumbnails/chris_retro_arcade.jpg',
    'description': "An arcade filled with classic machines from the 80s and 90s. Pinball, fighting games, racing cabinets, "
                "and a few rare finds. It's loud, nostalgic, and meant to feel like old school gaming again. "
                "Half-price entry on Sundays.",
    'lat': 37.079511,
    'lon': -76.520144,
    'tags': [19, 27, 64, 66]},
  {'title': "Olivia's Outdoor Gear",
    'category': 'retail',
    'thumbnail': 'resources/images/business_thumbnails/olivias_outdoor_gear.jpg',
    'description': "Outdoor equipment for hiking, camping, and beginner adventurers. I focus on durable gear that isn't "
                "ridiculously overpriced. Staff are happy to help new hikers figure out what they actually need. "
                "Use code TRAIL15 for 15% off select gear.",
    'lat': 37.054399,
    'lon': -76.495722,
    'tags': [39, 84, 88]},
  {'title': "Dave's Detailing",
    'category': 'services',
    'thumbnail': 'resources/images/business_thumbnails/daves_detailing.jpg',
    'description': "Car detailing service focused on making your vehicle look brand new. Interior and exterior "
                "packages available. Use code CLEAN15 for 15% off your first visit.",
    'lat': 37.085277,
    'lon': -76.486311,
    'tags': [60, 85, 88]},
  {'title': "Lily's Library Lounge",
    'category': 'entertainment',
    'thumbnail': 'resources/images/business_thumbnails/lilys_library_lounge.jpg',
    'description': "A quiet reading lounge with comfy seating and a large selection of books. Perfect for studying "
                "or relaxing. Free tea is included with entry, and students get discounted admission.",
    'lat': 37.063188,
    'lon': -76.473955,
    'tags': [33, 79, 86]},
  {'title': "Noah's Tech Hub",
    'category': 'retail',
    'thumbnail': 'resources/images/business_thumbnails/noahs_tech_hub.jpg',
    'description': "Electronics store offering accessories, repairs, and custom PC help. Staff are knowledgeable and "
                "honest about what you actually need. Students get 10% off with ID.",
    'lat': 37.097144,
    'lon': -76.492288,
    'tags': [32, 74, 75, 88]},
  {'title': "Zoe's Fitness Studio",
    'category': 'services',
    'thumbnail': 'resources/images/business_thumbnails/zoes_fitness_studio.jpg',
    'description': "Small group fitness classes focused on strength and conditioning. Sessions are high energy and "
                "beginner friendly. First class is free for new members.",
    'lat': 37.071022,
    'lon': -76.515933,
    'tags': [41, 44, 88]},
 {'title': 'Harbor Roast Cafe',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/harbor_roast_cafe.jpg',
  'description': 'A cozy neighborhood cafe serving espresso drinks, breakfast sandwiches, and pastries. First-time '
                 'guests can use a 10% off coupon.',
  'lat': 35.960691,
  'lon': -77.522347,
  'tags': [1, 3, 4, 88]},
 {'title': 'Tidal Spoon Bistro',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/tidal_spoon_bistro.jpg',
  'description': 'A casual bistro with comfort plates, soups, and rotating seasonal specials. Show this listing for a '
                 'free drink with your order.',
  'lat': 37.111163,
  'lon': -76.480171,
  'tags': [1, 86, 88, 93]},
 {'title': 'Biscuit Bay Bakery',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/biscuit_bay_bakery.jpg',
  'description': 'A small bakery known for biscuits, muffins, and fresh daily pastries. Weekend specials include a '
                 'small discount on your total.',
  'lat': 37.715222,
  'lon': -76.872093,
  'tags': [1, 5, 88, 85]},
 {'title': 'Coastal Crumb Patisserie',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/coastal_crumb_patisserie.jpg',
  'description': 'A dessert shop focused on cakes, tarts, and hand-finished sweets. First-time guests can use a 10% '
                 'off coupon.',
  'lat': 37.865086,
  'lon': -76.244472,
  'tags': [1, 6, 88, 87]},
 {'title': 'Salt & Smoke BBQ',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/salt_and_smoke_bbq.jpg',
  'description': 'A barbecue counter serving smoked meats, sides, and classic plates. First-time guests can use a 10% '
                 'off coupon.',
  'lat': 36.987163,
  'lon': -76.615643,
  'tags': [1, 11, 88, 86]},
 {'title': 'Pier 17 Deli',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/pier_17_deli.jpg',
  'description': 'A deli with stacked sandwiches, soups, and quick lunch specials. Weekend specials include a small '
                 'discount on your total.',
  'lat': 37.606009,
  'lon': -77.896696,
  'tags': [1, 9, 88, 85]},
 {'title': 'Boardwalk Slice Pizza',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/boardwalk_slice_pizza.jpg',
  'description': 'A pizza shop offering slices, whole pies, and affordable family combos. Show this listing for a free '
                 'drink with your order.',
  'lat': 37.201657,
  'lon': -76.488629,
  'tags': [1, 7, 88, 86, 91]},
 {'title': 'Dockside Dumplings',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/dockside_dumplings.jpg',
  'description': 'A small kitchen serving dumplings, noodle bowls, and shareable appetizers. First-time guests can use '
                 'a 10% off coupon.',
  'lat': 36.894533,
  'lon': -76.535227,
  'tags': [1, 12, 88, 86, 93]},
 {'title': 'Mango Moon Thai',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/mango_moon_thai.jpg',
  'description': 'A Thai restaurant with curry bowls, noodle dishes, and takeout-friendly meals. Show this listing for '
                 'a free drink with your order.',
  'lat': 37.380373,
  'lon': -76.285358,
  'tags': [1, 12, 88, 86]},
 {'title': 'La Ola Taqueria',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/la_ola_taqueria.jpg',
  'description': 'A bright taqueria with tacos, burritos, and weekend lunch deals. Weekend specials include a small '
                 'discount on your total.',
  'lat': 36.477468,
  'lon': -76.5217,
  'tags': [1, 13, 88, 85, 91]},
 {'title': 'Noodle Tide',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/noodle_tide.jpg',
  'description': 'A noodle bar with ramen, stir-fries, and fast weekday lunch specials. First-time guests can use a '
                 '10% off coupon.',
  'lat': 36.895029,
  'lon': -76.685499,
  'tags': [1, 12, 88, 86, 93]},
 {'title': 'Green Fork Vegan Kitchen',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/green_fork_vegan_kitchen.jpg',
  'description': 'A plant-based kitchen offering bowls, wraps, and fresh vegan meals. Show this listing for a free '
                 'drink with your order.',
  'lat': 37.078119,
  'lon': -76.551253,
  'tags': [1, 16, 17, 88, 93]},
 {'title': 'Sunrise Smoothies',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/sunrise_smoothies.jpg',
  'description': 'A healthy drink stop with smoothies, acai bowls, and quick grab-and-go options. First-time guests '
                 'can use a 10% off coupon.',
  'lat': 36.969183,
  'lon': -76.717238,
  'tags': [1, 17, 88, 85, 91]},
 {'title': 'Blue Crab Seafood Shack',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/blue_crab_seafood_shack.jpg',
  'description': 'A seafood shack serving fried baskets, crab dishes, and coastal favorites. First-time guests can use '
                 'a 10% off coupon.',
  'lat': 37.015289,
  'lon': -76.0522,
  'tags': [1, 15, 88, 86]},
 {'title': 'Creamline Ice Cream',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/creamline_ice_cream.jpg',
  'description': 'An ice cream shop with cones, sundaes, and rotating seasonal flavors. Weekend specials include a '
                 'small discount on your total.',
  'lat': 37.006546,
  'lon': -76.534181,
  'tags': [1, 10, 6, 88, 94]},
 {'title': 'Route 60 Burger House',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/route_60_burger_house.jpg',
  'description': 'A burger spot with hand-pressed patties, fries, and late-night specials. First-time guests can use a '
                 '10% off coupon.',
  'lat': 37.37957,
  'lon': -76.434493,
  'tags': [1, 8, 88, 86, 90]},
 {'title': 'Corner Café',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/corner_cafe.jpg',
  'description': 'A small coffee counter serving drip coffee, lattes, and light breakfast items. First-time guests can '
                 'use a 10% off coupon.',
  'lat': 37.282125,
  'lon': -76.200939,
  'tags': [1, 3, 4, 88, 93]},
 {'title': 'Southside Sandwiches',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/southside_sandwiches.jpg',
  'description': 'A sandwich shop with hot subs, wraps, and easy lunch pickup. Show this listing for a free drink with '
                 'your order.',
  'lat': 36.789666,
  'lon': -76.924195,
  'tags': [1, 9, 88, 85, 91]},
 {'title': 'The Daily Brunch',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/the_daily_brunch.jpg',
  'description': 'A brunch café with omelets, pancakes, and weekend specials. First-time guests can use a 10% off '
                 'coupon.',
  'lat': 36.908572,
  'lon': -76.521302,
  'tags': [1, 86, 88, 93, 94]},
 {'title': 'Bayberry Bistro',
  'category': 'food',
  'thumbnail': 'resources/images/business_thumbnails/bayberry_bistro.jpg',
  'description': 'An upscale neighborhood bistro with pasta, seafood, and date-night plates. Weekend specials include '
                 'a small discount on your total.',
  'lat': 37.086473,
  'lon': -76.455285,
  'tags': [1, 14, 88, 87, 93]},
 {'title': 'Harbor Threads',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/harbor_threads.jpg',
  'description': 'A clothing shop with casual outfits, seasonal basics, and affordable styles. New customers can use a '
                 '10% off coupon on their first purchase.',
  'lat': 37.259895,
  'lon': -76.379293,
  'tags': [30, 88, 86, 95]},
 {'title': 'Seaside Sneakers',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/seaside_sneakers.jpg',
  'description': 'A shoe store with athletic pairs, casual sneakers, and comfort-focused options. New customers can '
                 'use a 10% off coupon on their first purchase.',
  'lat': 37.248232,
  'lon': -77.000442,
  'tags': [31, 88, 86, 95]},
 {'title': 'TideTech',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/tidetech.jpg',
  'description': 'An electronics shop for accessories, small gadgets, and simple tech upgrades. New customers can use '
                 'a 10% off coupon on their first purchase.',
  'lat': 38.111019,
  'lon': -76.642171,
  'tags': [32, 88, 86, 95]},
 {'title': 'Paper Moon Bookshop',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/paper_moon_bookshop.jpg',
  'description': 'An independent bookstore with fiction, gifts, and a quiet browsing space. Seasonal sales include a '
                 'small discount on selected items.',
  'lat': 37.162093,
  'lon': -75.608271,
  'tags': [33, 88, 85, 95]},
 {'title': 'Market Basket Grocer',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/market_basket_grocer.jpg',
  'description': 'A small grocery with produce, pantry staples, and everyday essentials. Seasonal sales include a '
                 'small discount on selected items.',
  'lat': 37.737683,
  'lon': -75.866539,
  'tags': [34, 88, 85, 95]},
 {'title': 'QuickStop Convenience',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/quickstop_convenience.jpg',
  'description': 'A convenience store for snacks, drinks, and late-night basics. Show this listing for a free add-on '
                 'with qualifying orders.',
  'lat': 37.572408,
  'lon': -75.300448,
  'tags': [35, 88, 85, 90]},
 {'title': 'Willow Furnishings',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/willow_furnishings.jpg',
  'description': 'A furniture store with sofas, tables, and home setup pieces. New customers can use a 10% off coupon '
                 'on their first purchase.',
  'lat': 36.846629,
  'lon': -76.629429,
  'tags': [36, 88, 87, 95]},
 {'title': 'Home Harbor Goods',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/home_harbor_goods.jpg',
  'description': 'A home goods shop with kitchen items, décor, and apartment essentials. New customers can use a 10% '
                 'off coupon on their first purchase.',
  'lat': 37.063869,
  'lon': -76.545351,
  'tags': [37, 88, 86, 95]},
 {'title': 'Pearl & Pine Jewelry',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/pearl_and_pine_jewelry.jpg',
  'description': 'A jewelry boutique with simple chains, rings, and gift-ready pieces. Show this listing for a free '
                 'add-on with qualifying orders.',
  'lat': 37.110115,
  'lon': -76.512664,
  'tags': [38, 88, 87, 95]},
 {'title': 'Shoreline Sporting Goods',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/shoreline_sporting_goods.jpg',
  'description': 'A sporting goods store for team gear, training accessories, and outdoor supplies. New customers can '
                 'use a 10% off coupon on their first purchase.',
  'lat': 36.905472,
  'lon': -76.554921,
  'tags': [39, 88, 86, 95]},
 {'title': 'Coastal Thrift',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/coastal_thrift.jpg',
  'description': 'A thrift shop with secondhand clothes, shoes, and budget-friendly finds. New customers can use a 10% '
                 'off coupon on their first purchase.',
  'lat': 37.059122,
  'lon': -76.367613,
  'tags': [40, 88, 85, 95]},
 {'title': 'Pixel Point Electronics',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/pixel_point_electronics.jpg',
  'description': 'A tech shop with headphones, chargers, and small electronics. Seasonal sales include a small '
                 'discount on selected items.',
  'lat': 36.584014,
  'lon': -76.257645,
  'tags': [32, 88, 86, 95]},
 {'title': 'Outfit Outlet',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/outfit_outlet.jpg',
  'description': 'An outlet store with discounted clothing and clearance racks. New customers can use a 10% off coupon '
                 'on their first purchase.',
  'lat': 36.881066,
  'lon': -76.36964,
  'tags': [30, 88, 85, 95]},
 {'title': 'Lantern Housewares',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/lantern_housewares.jpg',
  'description': 'A home store with mugs, storage pieces, and practical décor. New customers can use a 10% off coupon '
                 'on their first purchase.',
  'lat': 37.03219,
  'lon': -76.523153,
  'tags': [37, 88, 86, 95]},
 {'title': 'Wave Watchers Gear',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/wave_watchers_gear.jpg',
  'description': 'An outdoor gear shop with backpacks, water bottles, and trip essentials. Show this listing for a '
                 'free add-on with qualifying orders.',
  'lat': 36.934836,
  'lon': -76.36127,
  'tags': [39, 88, 86, 95]},
 {'title': 'Bay Books & Gifts',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/bay_books_and_gifts.jpg',
  'description': 'A bookstore-gift shop with reads, journals, and small gift items. Show this listing for a free '
                 'add-on with qualifying orders.',
  'lat': 36.996539,
  'lon': -76.497144,
  'tags': [33, 88, 85, 95]},
 {'title': 'Dockside Decor',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/dockside_decor.jpg',
  'description': 'A décor and furniture shop with accent pieces and room updates. Show this listing for a free add-on '
                 'with qualifying orders.',
  'lat': 36.843441,
  'lon': -76.542927,
  'tags': [36, 88, 87, 95]},
 {'title': 'Anchor Apparel',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/anchor_apparel.jpg',
  'description': 'A clothing store with casual wear, work basics, and layered looks. Show this listing for a free '
                 'add-on with qualifying orders.',
  'lat': 37.447106,
  'lon': -76.71193,
  'tags': [30, 88, 86, 95]},
 {'title': 'Neon Nook Gaming Store',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/neon_nook_gaming_store.jpg',
  'description': 'A gaming store with tabletop items, hobby supplies, and collectibles. New customers can use a 10% '
                 'off coupon on their first purchase.',
  'lat': 37.022703,
  'lon': -76.612336,
  'tags': [77, 88, 86, 95]},
 {'title': 'Harbor Optical',
  'category': 'retail',
  'thumbnail': 'resources/images/business_thumbnails/harbor_optical.jpg',
  'description': 'An eyewear shop with frames, lenses, and accessories. New customers can use a 10% off coupon on '
                 'their first purchase.',
  'lat': 37.821717,
  'lon': -75.919144,
  'tags': [32, 88, 86, 95]},
 {'title': 'Neon Harbor Bowling',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/neon_harbor_bowling.jpg',
  'description': 'A bowling alley with leagues, casual games, and weekend specials. Use this listing for a discounted '
                 'entry price on select days.',
  'lat': 36.948563,
  'lon': -76.457632,
  'tags': [18, 79, 88, 90]},
 {'title': 'Atomic Arcade',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/atomic_arcade.jpg',
  'description': 'An arcade packed with classic cabinets, prizes, and coin-op games. Use this listing for a discounted '
                 'entry price on select days.',
  'lat': 36.310362,
  'lon': -75.211768,
  'tags': [19, 79, 80, 88, 90]},
 {'title': 'Moonlight Cinema',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/moonlight_cinema.jpg',
  'description': 'A movie theater with new releases, matinees, and snack combos. Weeknight visits often come with a '
                 'reduced-price special.',
  'lat': 37.049578,
  'lon': -77.042935,
  'tags': [20, 79, 80, 88, 90]},
 {'title': 'Tide Escape Rooms',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/tide_escape_rooms.jpg',
  'description': 'An escape-room venue with themed puzzles and group challenges. Weeknight visits often come with a '
                 'reduced-price special.',
  'lat': 37.142996,
  'lon': -76.271662,
  'tags': [22, 79, 80, 81, 88]},
 {'title': 'Seaside Mini Golf',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/seaside_mini_golf.jpg',
  'description': 'A mini golf course with family-friendly holes and outdoor play. Birthday and group bookings can '
                 'include a small coupon deal.',
  'lat': 36.727572,
  'lon': -76.082921,
  'tags': [23, 79, 84, 88, 94]},
 {'title': 'Harbor Stage Theatre',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/harbor_stage_theatre.jpg',
  'description': 'A theater venue hosting plays, performances, and student nights. Birthday and group bookings can '
                 'include a small coupon deal.',
  'lat': 37.168212,
  'lon': -76.400672,
  'tags': [25, 79, 80, 82, 88]},
 {'title': 'Rhythm Room Karaoke',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/rhythm_room_karaoke.jpg',
  'description': 'A karaoke spot with private rooms, drinks, and late-night sessions. Use this listing for a '
                 'discounted entry price on select days.',
  'lat': 36.872651,
  'lon': -76.518595,
  'tags': [29, 80, 83, 88, 90]},
 {'title': 'LiveWire Music Hall',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/livewire_music_hall.jpg',
  'description': 'A music hall with live bands, open mic nights, and ticket specials. Birthday and group bookings can '
                 'include a small coupon deal.',
  'lat': 37.718772,
  'lon': -76.35802,
  'tags': [24, 80, 83, 88, 90]},
 {'title': 'Pixel Play Gaming Lounge',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/pixel_play_gaming_lounge.jpg',
  'description': 'A gaming lounge for console play, tournaments, and friend hangouts. Use this listing for a '
                 'discounted entry price on select days.',
  'lat': 37.054772,
  'lon': -75.996832,
  'tags': [27, 79, 80, 88, 90]},
 {'title': 'Waves VR Arena',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/waves_vr_arena.jpg',
  'description': 'A VR arena with headset games, multiplayer sessions, and party bookings. Weeknight visits often come '
                 'with a reduced-price special.',
  'lat': 37.547294,
  'lon': -76.397329,
  'tags': [28, 79, 80, 88, 90]},
 {'title': 'Boardwalk Bounce',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/boardwalk_bounce.jpg',
  'description': 'An amusement-style play center with group activities and birthday packages. Use this listing for a '
                 'discounted entry price on select days.',
  'lat': 37.561563,
  'lon': -75.572502,
  'tags': [21, 79, 81, 84, 88]},
 {'title': 'Lighthouse Lanes',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/lighthouse_lanes.jpg',
  'description': 'A bowling spot with lane rentals, shoes, and casual league play. Birthday and group bookings can '
                 'include a small coupon deal.',
  'lat': 37.285098,
  'lon': -77.181827,
  'tags': [18, 79, 80, 88, 90]},
 {'title': "Mariner's Magic Show",
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/mariners_magic_show.jpg',
  'description': 'A live performance venue featuring stage magic and family shows. Use this listing for a discounted '
                 'entry price on select days.',
  'lat': 37.151953,
  'lon': -76.573753,
  'tags': [25, 79, 80, 82, 88]},
 {'title': 'Sunset Sports Center',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/sunset_sports_center.jpg',
  'description': 'A sports venue for open play, pickup games, and weekend matches. Use this listing for a discounted '
                 'entry price on select days.',
  'lat': 37.108492,
  'lon': -76.592618,
  'tags': [26, 79, 84, 88, 94]},
 {'title': 'Harbor Haunt Nights',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/harbor_haunt_nights.jpg',
  'description': 'A nightlife venue with themed events, evening entertainment, and cover specials. Birthday and group '
                 'bookings can include a small coupon deal.',
  'lat': 37.082955,
  'lon': -76.525937,
  'tags': [83, 80, 82, 88, 90]},
 {'title': 'Open Sky Amphitheater',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/open_sky_amphitheater.jpg',
  'description': 'An outdoor performance space for concerts, festivals, and summer shows. Use this listing for a '
                 'discounted entry price on select days.',
  'lat': 36.203175,
  'lon': -75.608323,
  'tags': [24, 80, 82, 84, 88]},
 {'title': 'Coastline Comedy Club',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/coastline_comedy_club.jpg',
  'description': 'A comedy club with stand-up nights, open mic spots, and discount cover. Use this listing for a '
                 'discounted entry price on select days.',
  'lat': 37.028287,
  'lon': -76.570091,
  'tags': [25, 80, 82, 88, 90]},
 {'title': 'Bayfront Birthday Zone',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/bayfront_birthday_zone.jpg',
  'description': 'A party venue that hosts birthday packages and small celebrations. Birthday and group bookings can '
                 'include a small coupon deal.',
  'lat': 37.020673,
  'lon': -76.52152,
  'tags': [81, 79, 82, 88]},
 {'title': 'Dockside Event Hall',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/dockside_event_hall.jpg',
  'description': 'An event hall for private gatherings, receptions, and meetings. Weeknight visits often come with a '
                 'reduced-price special.',
  'lat': 37.433913,
  'lon': -76.826744,
  'tags': [82, 79, 81, 88]},
 {'title': 'Starlight Family Fun',
  'category': 'entertainment',
  'thumbnail': 'resources/images/business_thumbnails/starlight_family_fun.jpg',
  'description': 'A family entertainment center with games, snacks, and group deals. Use this listing for a discounted '
                 'entry price on select days.',
  'lat': 37.046541,
  'lon': -76.516632,
  'tags': [79, 81, 84, 88, 94]},
 {'title': 'Clip & Clipper Barber Shop',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/clip_and_clipper_barber_shop.jpg',
  'description': 'A barber shop for fades, trims, and quick neighborhood cuts. Selected appointments include a small '
                 'first-time discount.',
  'lat': 37.174058,
  'lon': -76.409521,
  'tags': [58, 88, 85, 90]},
 {'title': 'Fresh Fade Studio',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/fresh_fade_studio.jpg',
  'description': 'A hair salon offering cuts, styling, and easy maintenance packages. Mention this listing to get a '
                 'discounted first visit.',
  'lat': 37.082708,
  'lon': -76.205331,
  'tags': [57, 88, 86, 90]},
 {'title': 'Spark Auto Repair',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/spark_auto_repair.jpg',
  'description': 'An auto repair shop handling diagnostics, brakes, and maintenance work. Selected appointments '
                 'include a small first-time discount.',
  'lat': 37.057268,
  'lon': -76.426157,
  'tags': [60, 88, 86, 95]},
 {'title': 'Harbor Wash Car Care',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/harbor_wash_car_care.jpg',
  'description': 'A car wash and detailing stop for regular cleanups and interior care. New clients can use a coupon '
                 'for a percentage off their service.',
  'lat': 36.756908,
  'lon': -76.003149,
  'tags': [61, 88, 85, 95]},
 {'title': 'Nook Nail Studio',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/nook_nail_studio.jpg',
  'description': 'A nail studio offering manicures, pedicures, and simple nail art. New clients can use a coupon for a '
                 'percentage off their service.',
  'lat': 37.091937,
  'lon': -76.395417,
  'tags': [59, 88, 86, 95]},
 {'title': 'Tide Pet Grooming',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/tide_pet_grooming.jpg',
  'description': 'A pet grooming shop with baths, trims, and coat care. New clients can use a coupon for a percentage '
                 'off their service.',
  'lat': 37.077637,
  'lon': -76.437576,
  'tags': [67, 88, 85, 95]},
 {'title': 'Anchor Insurance',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/anchor_insurance.jpg',
  'description': 'An insurance office helping with coverage, quotes, and policy reviews. Selected appointments include '
                 'a small first-time discount.',
  'lat': 37.160966,
  'lon': -76.4938,
  'tags': [62, 88, 87, 95]},
 {'title': 'Legal Harbor',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/legal_harbor.jpg',
  'description': 'A legal services office offering consultations and document help. New clients can use a coupon for a '
                 'percentage off their service.',
  'lat': 37.0412,
  'lon': -76.027987,
  'tags': [63, 88, 87, 95]},
 {'title': 'Ledger Financial',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/ledger_financial.jpg',
  'description': 'A financial services office with tax prep, budgeting, and planning support. Mention this listing to '
                 'get a discounted first visit.',
  'lat': 36.690634,
  'lon': -76.193182,
  'tags': [64, 88, 87, 95]},
 {'title': 'Seaside Realty',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/seaside_realty.jpg',
  'description': 'A real estate office helping buyers, renters, and sellers. New clients can use a coupon for a '
                 'percentage off their service.',
  'lat': 37.055039,
  'lon': -76.505653,
  'tags': [65, 88, 87, 95]},
 {'title': 'Bright Clean Services',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/bright_clean_services.jpg',
  'description': 'A cleaning business for homes, offices, and recurring service visits. Mention this listing to get a '
                 'discounted first visit.',
  'lat': 37.670302,
  'lon': -76.281283,
  'tags': [66, 88, 85, 95]},
 {'title': 'Pedal Pro Bike Repair',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/pedal_pro_bike_repair.jpg',
  'description': 'A bike repair shop for tune-ups, flats, and brake adjustments. New clients can use a coupon for a '
                 'percentage off their service.',
  'lat': 37.584015,
  'lon': -77.508476,
  'tags': [60, 88, 86, 95]},
 {'title': 'Fit Harbor Gym',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/fit_harbor_gym.jpg',
  'description': 'A compact gym with strength equipment, cardio, and beginner-friendly plans. Mention this listing to '
                 'get a discounted first visit.',
  'lat': 37.031366,
  'lon': -76.421835,
  'tags': [41, 88, 86, 95]},
 {'title': 'Flow Yoga Studio',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/flow_yoga_studio.jpg',
  'description': 'A yoga studio with calming classes, stretching, and beginner sessions. Selected appointments include '
                 'a small first-time discount.',
  'lat': 36.769242,
  'lon': -75.7539,
  'tags': [42, 88, 86, 95]},
 {'title': 'Iron Tide Martial Arts',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/iron_tide_martial_arts.jpg',
  'description': 'A martial arts studio with self-defense, discipline, and family classes. Mention this listing to get '
                 'a discounted first visit.',
  'lat': 36.485508,
  'lon': -77.214589,
  'tags': [43, 88, 86, 95]},
 {'title': 'Peak Personal Training',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/peak_personal_training.jpg',
  'description': 'A personal training studio with one-on-one coaching and custom programs. Selected appointments '
                 'include a small first-time discount.',
  'lat': 36.725947,
  'lon': -76.480645,
  'tags': [44, 88, 87, 95]},
 {'title': 'Coastal Physical Therapy',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/coastal_physical_therapy.jpg',
  'description': 'A physical therapy practice focused on recovery, mobility, and strength. Mention this listing to get '
                 'a discounted first visit.',
  'lat': 36.962872,
  'lon': -76.626569,
  'tags': [46, 88, 87, 95]},
 {'title': 'Wellness Bay Spa',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/wellness_bay_spa.jpg',
  'description': 'A spa offering massages, relaxation services, and wellness treatments. New clients can use a coupon '
                 'for a percentage off their service.',
  'lat': 36.080747,
  'lon': -76.154931,
  'tags': [47, 48, 88, 87, 95]},
 {'title': 'Brake & Tire Depot',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/brake_and_tire_depot.jpg',
  'description': 'A tire and brake service shop with inspections, installs, and balance work. New clients can use a '
                 'coupon for a percentage off their service.',
  'lat': 37.127867,
  'lon': -76.254436,
  'tags': [72, 88, 86, 95]},
 {'title': 'ByteFix Computer Repair',
  'category': 'services',
  'thumbnail': 'resources/images/business_thumbnails/bytefix_computer_repair.jpg',
  'description': 'A computer repair shop for hardware fixes, diagnostics, and upgrades. Mention this listing to get a '
                 'discounted first visit.',
  'lat': 37.087067,
  'lon': -76.74777,
  'tags': [74, 78, 88, 86, 95]}]

sample_review_texts = (
    [
        "Really enjoyed {title}. The staff were friendly and the experience felt smooth.",
        "Great visit to {title}. The prices felt fair and the quality matched the hype.",
        "I would definitely come back to {title}. Everything was clean, quick, and easy.",
        "{title} made a strong first impression and the service was solid.",
    ],
    [
        "{title} was fine overall, but there were a few small issues.",
        "Decent experience at {title}. Not amazing, but not bad either.",
        "The visit to {title} was okay. Some parts were good and some felt average.",
        "{title} did the job, though I expected a little more.",
    ],
    [
        "I was disappointed by {title}. The experience felt slower than expected.",
        "{title} did not quite live up to my expectations.",
        "There were too many issues at {title} for me to recommend it.",
        "My visit to {title} was rough and I probably would not rush back.",
    ]
    )

preset_tags = [
    'Restaurant',
    'Fast Food',
    'Cafe',
    'Coffee',
    'Bakery',
    'Dessert',
    'Pizza',
    'Burger',
    'Sandwich',
    'Ice Cream',
    'Barbecue',
    'Asian Cuisine',
    'Mexican Cuisine',
    'Italian Cuisine',
    'Seafood',
    'Vegan',
    'Healthy Food',
    'Bowling',
    'Arcade',
    'Cinema',
    'Amusement Park',
    'Escape Room',
    'Mini Golf',
    'Live Music',
    'Theater',
    'Sports Venue',
    'Gaming',
    'VR Experience',
    'Karaoke',
    'Clothing',
    'Shoes',
    'Electronics',
    'Bookstore',
    'Grocery Store',
    'Convenience Store',
    'Furniture',
    'Home Goods',
    'Jewelry',
    'Sporting Goods',
    'Thrift Store',
    'Gym',
    'Yoga',
    'Martial Arts',
    'Personal Training',
    'Sports Club',
    'Physical Therapy',
    'Spa',
    'Wellness',
    'Tutoring',
    'School',
    'College Prep',
    'Music Lessons',
    'Art Classes',
    'STEM Learning',
    'Driving School',
    'Language Learning',
    'Hair Salon',
    'Barber Shop',
    'Nail Salon',
    'Auto Repair',
    'Car Wash',
    'Insurance',
    'Legal Services',
    'Financial Services',
    'Real Estate',
    'Cleaning Services',
    'Pet Grooming',
    'Veterinary',
    'Car Dealership',
    'Auto Parts',
    'Oil Change',
    'Tire Shop',
    'Motorcycle Service',
    'Computer Repair',
    'Software Services',
    'IT Services',
    'Gaming Store',
    'Electronics Repair',
    'Family Friendly',
    'Date Night',
    'Birthday Parties',
    'Event Hosting',
    'Nightlife',
    'Outdoor Activities',
    'Cheap',
    'Mid Range',
    'Luxury',
    'Local Owned',
    'Chain',
    'Open Late',
    'Takeout',
    'Delivery',
    'Dine In',
    'Outdoor Seating',
    'Wheelchair Accessible'
]

def add_fake_users():
    for username in sample_usernames:
        add_user(username, "password", 37.0479891178922, -76.4984552293407)

def add_fake_businesses():
    for index, business in enumerate(sample_businesses):
        owner_id = index + 1
        add_business(
            business["title"],
            owner_id,
            business["category"],
            business["thumbnail"],
            business["description"],
            business["lat"],
            business["lon"],
        )

def add_fake_reviews():
    positive, mixed, negative = sample_review_texts
    for index, business in enumerate(sample_businesses):
        business_id = index + 1
        owner_id = index + 1
        rnd = random.Random(20260609 + business_id)

        quality_roll = rnd.random()
        if quality_roll < 0.15:
            ratings = [3.0, 2.5, 2.0, 1.5]
        elif quality_roll < 0.35:
            ratings = [4.0, 3.5, 3.0, 2.5]
        elif quality_roll < 0.72:
            ratings = [4.5, 4.0, 3.5, 3.0]
        else:
            ratings = [5.0, 4.5, 4.0, 3.5]

        reviewer_pool = [u for u in range(1, len(sample_usernames)) if u != owner_id]
        reviewer_ids = rnd.sample(reviewer_pool, 4)

        text_sets = [
            (ratings[0], rnd.choice(positive)),
            (ratings[1], rnd.choice(positive + mixed)),
            (ratings[2], rnd.choice(mixed)),
            (ratings[3], rnd.choice(negative if ratings[3] <= 2.5 else mixed)),
        ]

        for user_id, (rating, template) in zip(reviewer_ids, text_sets):
            review_text = template.format(title=business["title"])
            #Add noise
            rating = min(rating + (rnd.randint(0,1)-.5)*rnd.randint(-1, 1), 5)
            add_review(user_id, business_id, rating, review_text)

def add_preset_tags():
    for tag in preset_tags:
        add_preset_tag(tag)

def set_fake_tags():
    for index, business in enumerate(sample_businesses):
        business_id = index + 1
        for tag_id in business["tags"]:
            set_business_tag(business_id, tag_id)

def generate_all_fake_data():
    add_fake_users()
    add_fake_businesses()
    add_fake_reviews()
    add_preset_tags()
    set_fake_tags()

DATA_AMOUNT = 15

def add_some_fake_users():
    for username in sample_usernames[:DATA_AMOUNT]:
        add_user(username, "password", 37.0479891178922, -76.4984552293407)

def add_some_fake_businesses():
    for index, business in enumerate(sample_businesses[:DATA_AMOUNT]):
        owner_id = index + 1
        add_business(
            business["title"],
            owner_id,
            business["category"],
            business["thumbnail"],
            business["description"],
            business["lat"],
            business["lon"],
        )

def add_some_fake_reviews():
    positive, mixed, negative = sample_review_texts

    for index, business in enumerate(sample_businesses[:DATA_AMOUNT]):
        business_id = index + 1
        owner_id = index + 1
        rnd = random.Random(20260609 + business_id)

        quality_roll = rnd.random()
        if quality_roll < 0.15:
            ratings = [3.0, 2.5, 2.0, 1.5]
        elif quality_roll < 0.35:
            ratings = [4.0, 3.5, 3.0, 2.5]
        elif quality_roll < 0.72:
            ratings = [4.5, 4.0, 3.5, 3.0]
        else:
            ratings = [5.0, 4.5, 4.0, 3.5]

        reviewer_pool = [u for u in range(1, min(len(sample_usernames[:DATA_AMOUNT]), 25)) if u != owner_id]
        reviewer_ids = rnd.sample(reviewer_pool, 4)

        text_sets = [
            (ratings[0], rnd.choice(positive)),
            (ratings[1], rnd.choice(positive + mixed)),
            (ratings[2], rnd.choice(mixed)),
            (ratings[3], rnd.choice(negative if ratings[3] <= 2.5 else mixed)),
        ]

        for user_id, (rating, template) in zip(reviewer_ids, text_sets):
            review_text = template.format(title=business["title"])
            #Add noise
            rating = min(rating + (rnd.randint(0,1)-.5)*rnd.randint(-1, 1), 5)
            add_review(user_id, business_id, rating, review_text)

def set_some_fake_tags():
    for index, business in enumerate(sample_businesses[:DATA_AMOUNT]):
        business_id = index + 1
        for tag_id in business["tags"]:
            set_business_tag(business_id, tag_id)

def generate_some_fake_data():
    add_some_fake_users()
    add_some_fake_businesses()
    add_some_fake_reviews()
    add_preset_tags()
    set_some_fake_tags()
    