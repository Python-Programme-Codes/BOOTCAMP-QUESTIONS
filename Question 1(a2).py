#Social Media Post Analysis: (10 Marks)
#Write a program where the user inputs a social media post. The program should:

#Count the number of words in the post. (hint: split function)
#Return the hashtags as a list as well as the count of hashtags in the post (words starting with #).
#sample post:

#Work hard, play harder! #success #motivation #success

#Expected output:

#Enter your social media post: "Work hard, play harder! #success #motivation #success"
#Number of words: 7
#Number of hashtags: 3
#['#success', '#motivation', '#success"']

#-----------------------------------Part 1--------------------------------------------------
post = input("Enter your social media post:")
words =0
hashtags =0
#split_string = post.split()
#for word in split_string:
#    words+=1
#    if word.startswith("#"):
#        hashtags+=1
#
#print("Number of words:",words)
#print("Number of hashtags:",hashtags)

#-----------------------------------Part 2--------------------------------------------------

def show_hashtags(posts):
    hashtag = []
    split_string = posts.split()

    for word in split_string:
        if word.startswith("#"):
            hashtag.append(word)

    print(hashtag)



print("Number of hashtags:",hashtags)
show_hashtags(post)