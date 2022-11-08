import bs4
import requests

base_urls = {
    "mirror": "https://www.homedepot.com/b/Bath-Bathroom-Mirrors-Vanity-Mirrors/N-5yc1vZbzas",
    "bathtub": "https://www.homedepot.com/b/Bath-Bathtubs-Freestanding-Tubs/N-5yc1vZbz9d",
    "sink": "https://www.homedepot.com/b/Bath-Bathroom-Sinks-Drop-in-Bathroom-Sinks/N-5yc1vZbz9j",
    "shelf": "https://www.homedepot.com/b/Bath-Bathroom-Storage-Bathroom-Shelves/N-5yc1vZcfvz",
    "towel_bar": "https://www.homedepot.com/b/Bath-Bathroom-Accessories-Bathroom-Hardware-Towel-Bars/N-5yc1vZcfw6",
    "shower_curtain": "https://www.homedepot.com/b/Bath-Shower-Accessories-Shower-Curtains/N-5yc1vZcfv5",
    "vanity": "https://www.homedepot.com/b/Bath-Bathroom-Vanities-Bathroom-Vanities-with-Tops/N-5yc1vZcfw5",
    "faucet": "https://www.homedepot.com/b/Bath-Bathroom-Faucets-Bathroom-Sink-Faucets-Single-Hole-Bathroom-Faucets/N-5yc1vZbrg2",
    "shower_head": "https://www.homedepot.com/b/Bath-Bathroom-Faucets-Shower-Heads-Handheld-Shower-Heads/N-5yc1vZbrdj",
    "toilet": "https://www.homedepot.com/b/Bath-Toilets-One-Piece-Toilets/N-5yc1vZcb8v"
}

def get_html(url):
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"})
    soup = bs4.BeautifulSoup(r.text, features="lxml")
    print("\t\tGot HTML")
    return soup

def dl_imgs(c, img_urls):
    idx = 0
    for l in img_urls:
        print(f"\tDownloading Img: {c}_{idx}.png")
        r = requests.get(l)
        r.raw.decode_content = True
        with open(f"data/{c}_{idx}.png", "wb") as outfd:
            outfd.write(r.content)

        idx += 1

def get_category(key):
    base_url = base_urls[key]
    curr_url = base_url + "?Nao=0"
    img_urls = []

    while len(img_urls) < 100:
        print(f"\tGetting Page: {curr_url.split('?')[1]}")
        soup = get_html(curr_url)

        section1 = soup.find("section", {"id": "browse-search-pods-1"})
        section2 = soup.find("section", {"id": "browse-search-pods-2"})
        
        idx = 0

        for div in section1.childGenerator():
            if idx > 12:
                break
            img = div.find_next("img")
            if "productImages" in img.attrs["src"]:
                img_urls.append(img.attrs["src"])
                idx += 1

        separator_flag = True
        for div in section2.childGenerator():
            if idx > 23:
                break
            if separator_flag:
                separator_flag = False
                continue
            img = div.find_next("img")
            if "productImages" in img.attrs["src"]:
                img_urls.append(img.attrs["src"])
                idx += 1

        curr_url = base_url + f"?Nao={len(img_urls) + 1}"

    return img_urls[:100]

def main():
    for c in base_urls.keys():
        print(f"Getting Imgs for category: {c}")
        img_urls = get_category(c)
        print(f"DoWnloading Imgs for category: {c}")
        dl_imgs(c, img_urls)


if __name__ == "__main__":
    main()