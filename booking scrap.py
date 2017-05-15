import webbrowser, requests
from bs4 import BeautifulSoup
import unicodecsv as csv
import io

head = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"}
url = "https://www.booking.com/searchresults.html?label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaAKIAQGYATHCAQp3aW5kb3dzIDEwyAEM2AED6AEB-AECkgIBeagCAw;sid=ad12c08d3e125b2bf7f2107df75faa4f;checkin_month=5&checkin_monthday=15&checkin_year=2017&checkout_month=5&checkout_monthday=16&checkout_year=2017&class_interval=1&dest_id=-38833&dest_type=city&dtdisc=0&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&mih=0&no_rooms=1&offset=0&onclick_recs=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&src=index&src_elem=sb&ss=Marrakesh%2C%20Marrakech-Safi%2C%20Morocco&ss_all=0&ssb=empty&sshis=0&"
res = requests.get(url, headers=head)
soup = BeautifulSoup(res.text,"lxml")
hotels = soup.select("#hotellist_inner div.sr_item")

for hotel in hotels:
   #Hotel Name
   name = hotel.select_one("span.sr-hotel__name").text.strip()
   print("Hotel Name:"+name)
   #Hotel Rating
   score = hotel.select_one("span.average.js--hp-scorecard-scoreval")
   rating = score.text.strip()
   print("Hotel Rating:"+score.text.strip())
   #Hotel Price
   price = hotel.select_one("strong.price") 
   print("Hotel Price:"+price.text.strip() if price else "All rooms booked")
   #Hotel Code
   code= hotel.get('data-hotelid')
   print("Hotel Code:"+code)
   #hotel Rating
   star= hotel.select_one('span.invisible_spoken')
   starrating = star.text.strip()
   print("Hotel Type:"+starrating)
   #Hotel address
   address = hotel.select_one("a.jq_tooltip")
   address= address.text.strip()
   print("Hotel address:"+address) 
   #Hotel Coordinates
   for a in hotel.findAll('a'):
      coords= a.get('data-coords') 
      print (coords if coords else "")
      
   #writing to file 
   file = io.open("booking.csv", 'a', encoding='utf8') #change the name to save in txt file
   file.write('%r\n%r\n%r\n%r\n%r\n%r\n\n\n' % (name,starrating,rating,address,price.text.strip() if price else "All rooms booked",coords))
   file.close()
