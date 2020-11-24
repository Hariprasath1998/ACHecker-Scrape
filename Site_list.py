import csv

sites = ["Amazon.in", "eBay.in", "Flipkart.com", "Paytm.com", "SnapDeal.com", "Naaptol.com", "Limeroad.com", "Fabindia.com", "Infibeam.com", "HomeShop18.com", "IndiaTimes.com", "Shopping.rediff.com", "ShopClues.com", "Croma.com", "Zookr", "Zopper.com", "Latestone.com", "Gonoise.com", "Greendust.com", "Overcart.com", "Togofogo.com", "Valuecart.in", "Jabong.com", "Ajio.com", "StalkBuyLove.com", "Myntra.com", "Provogue.com", "6pm.com", "Coolwinks.com", "Yepme.com", "Bluestone.com", "Fashionandyou.com", "Shoppersstop.com", "Voonik.com", "Voylla.com", "Mirraw.com", "Caratlane.com", "Chrono24.in", "Indiarush.com", "Santana.in", "Faballey.com", "Nykaa.com", "Purplle.com", "Xotezo.com", "Newu.in", "Prettysecrets.com", "Koovs.com", "Clovia.com", "Shyaway.com", "Babyoye.com", "Firstcry.com", "Totaltoys.com", "Netmeds.com",
    "Healthkart.com", "Bookmyshow.com", "Redbus.in", "MakeMyTrip.com", "Yatra.com", "ClearTrip.com", "Expedia.co.in", "GoiBibo", "Ixigo.com", "Hotels.com", "Thomascook.in", "Travelguru.com", "Via.com", "Oyorooms", "Airbnb", "Booking.com", "Agoda.com", "Printvenue.com", "Printland.in", "Vistaprint.in", "Housefull.com", "Urbanladder.com", "Woodenstreet.com", "Craftsvilla.com", "Gaatha.com", "Homesake.in", "Vyomshop.com", "Handicraftshop.in", "Theindiacrafthouse.com", "Folkbridge.com", "Isayorganic.com", "Bigbasket.com", "Naturesbasket.co.in", "Go4fresh.in", "Teabox.com", "Buytea.com", "Prestogifts.com", "Fnp.com", "Archiesonline.com", "Giftcart.com", "Indiangiftsportal.com", "Decathlon.in", "Khelmart.com", "Sportsjam.in", "Sports365.in", "Dogspot.in", "Petsworld.in", "Pupkart.com", "Petshopindia.com", "Uread.com"]


with open('Analysis.csv', 'w') as csv_file:
	fieldnames=['Sites','Tested', 'Known', 'Likely', 'Potential']
	csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
	
	csv_writer.writeheader()

	for x in sites:
		csv_writer.writerow({'Sites':x,'Tested':'N'})