import nltk


def extract_entities(text):
    banned_list = ['Google', 'Add Grepper Answer', 'Add Writeup Image']
    person_list = []
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label'):
                if chunk.label() == 'PERSON':
                    if ' '.join(c[0] for c in chunk.leaves()) not in banned_list:
                        print(chunk.label(), '==>', ' '.join(c[0] for c in chunk.leaves()))
                        person_list.append(' '.join(c[0] for c in chunk.leaves()))
                        # return ' '.join(c[0] for c in chunk.leaves())
    return max(person_list, key=person_list.count)


if __name__ == '__main__':
    paragraph = """Skip to main contentAccessibility help
                    Accessibility feedback
                    Google
                    image...-title.jpg
                    image...-title.jpg
                    ×
                    susan b anthony stamp
                    
                    AllImages
                    More
                    Tools
                    About 536 results (1.76 seconds) « Add Grepper Answer (a)Add Writeup
                    
                    Image size:
                    1048 × 1200
                    Find other sizes of this image:
                    All sizes - Small - Medium
                    Possible related search: susan b anthony stamp
                    
                    Susan B. Anthony | National Postal Museumhttps://postalmuseum.si.edu › exhibition › susan-b-anth...
                    The 3-cent Susan B. Anthony stamp was issued on August 26, 1936. ... The U.S. Post Office issued the 50-cent Susan B. Anthony stamp in 1955, the 50th anniversary ...
                    
                    1051 – 1955 Liberty Series - 50¢ Susan B. Anthony - Mystic ...https://www.mysticstamp.com › United-States › USA
                    U.S. #1051 features an image of Susan B. Anthony based on a photograph from the Library of Congress. The stamp was issued exactly 50 years after the ...
                    Visually similar images
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Image result
                    Feedback
                    Pages that include matching images
                    
                    1936 Susan B Anthony Scott #784 3¢ Single US Postage Stamphttps://www.amazon.com › Susan-Anthony-Scott-Singl...
                    679 × 793 — Susan B. Anthony (1820-06) Women's Rights Pioneer Susan B. Anthony was selected to be the subject of the women's rights commemorative stamp.
                    
                    
                    Women's Right To Vote Susan B. Anthony Stamp and Coin ...https://www.michaels.com › ... › Coins & Currency
                    540 × 540 — The 3 cent postal stamp honors Women's Suffrage was first issued in Washington D.C. in 1936. The Susan B. Anthony dollar coin was minted from 1979 to 1999 and ...
                    
                    
                    3c Susan B. Anthony stamp - Google Arts & Culturehttps://artsandculture.google.com › asset
                    451 × 512 — Abolitionist, educator, labor leader, temperance worker and women's rights advocate Susan B. Anthony was born into a Massachusetts Quaker family in 1820.
                    
                    
                    The 11 Most Controversial Stamps in US Historyhttps://www.history.com › news › 11-most-controversia...
                    1048 × 1200 · 16-Apr-2018 — Susan B. Anthony stamp, released 1936. Some imaginative critics thought they saw a cigarette sticking out from the lips of the famous ...
                    
                    
                    Susan Anthony Stamps | Etsyhttps://www.etsy.com › market › susan_anthony_stamps
                    340 × 270 — Pack of 5 stamps .. 50c SUSAN B. ANTHONY stamp issued 1955 .. Vintage Unused US Postage Stamp | Women's Rights, Voting Rights, Feminism.
                    
                    1	
                    2
                    3
                    4
                    5
                    6
                    7
                    8
                    9
                    10
                    Next
                    Pakistan
                    Valencia, Lahore - From your IP address
                     - Update location
                    HelpSend feedbackPrivacyTerms"""
    print(extract_entities(paragraph))
