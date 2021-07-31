#this is program is written by Rigved Pulickal with the help of Aneesh Pulickal
email_sites = ["gmail.com", "yahoo.com", "twitter.com", "skype.com", "linkedin.in"]
email = input("enter your email: ")
email_split = email.split('@')
first_name = email_split[0].split('.')
if email_split[1] in email_sites:
    print("Hey " + first_name[0] + " heard you have a popular account - " + email_split[1])
else:
    print("Hey " + first_name[0] + " heard you have a (not to be rude) not popular account - " + email_split[1])