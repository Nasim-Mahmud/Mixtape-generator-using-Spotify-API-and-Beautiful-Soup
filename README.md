# Mixtape-generator-using-Spotify-API-and-Beautiful-Soup
In this project, I'll be developing a Mixtape generator that will generate a Spotify playlist of the top 100 songs based on any date that the user enters.

I have first made a variable using the Datetime module that will be applied at the end of the URL when scraping the data. I scraped the data from the <a href="https://www.billboard.com/charts/hot-100/">Billboard.com</a> website. The website's data was scraped using the BeautifulSoup package.
I pulled the top 100 songs of that specific date from the Billboard.com website once the user submitted the date. Now comes the challenging part.
We need a Spotify account to add those songs to a Spotify playlist. After signing into Spotify, we must create a Spotify App by visiting the  <a href="https://developer.spotify.com/dashboard/">developer dashboard</a>. Give it a name, and then click the Create An App button! Following that, an application interface will appear; copy the Client ID and Client Secret from there and add them to your project.

![My-Dashboard-Spotify-for-Developers](https://user-images.githubusercontent.com/57942968/193495755-8b3d19fc-f0db-4499-b795-b3aa825fa8ef.png)

NB: To prevent unwanted access to your account, you can convert these data into environment variables.
```
SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = "https://example.com/"
```

Spotify authentication might be a headache. Spotify uses OAuth to grant "secure delegated access" to client applications. OAuth uses access tokens rather than credentials to authenticate devices, APIs, servers, and apps while operating over HTTPS. I've used the <a href="https://pypi.org/project/spotipy/">Spotipy</a> module to authenticate Spotify. Additionally, the Spotify Dashboard's redirect URI needs to be specified.

![3](https://user-images.githubusercontent.com/57942968/193495942-d7dd3d92-d472-43e8-848b-9498f30ba3ff.png)
![4](https://user-images.githubusercontent.com/57942968/193495956-1257774a-55fe-4385-8399-d8024bc6b6ac.png)
 
I have used https://example.com as the redirect URI. After creating a SpotifyOAuth object and setting up the following parameters, run the code.

![5](https://user-images.githubusercontent.com/57942968/193496009-30bd8ceb-4318-45d1-ba40-9d431e4e3056.PNG)

 Then a webpage will open as follows, and we have to allow that access.
 
 ![7](https://user-images.githubusercontent.com/57942968/193496062-91b8dd95-83d7-459b-a758-41330d96cba0.png)
 
 After that, another window will be shown, and we have to copy the entire URL of that page and paste it into the code prompt. Paste it, and we will get a token.txt file. 

![Inked6](https://user-images.githubusercontent.com/57942968/193497082-4aa71e63-2e67-4da9-9fc2-287b8ab830d5.jpg)

We will be able to verify our authentication using this. The user id must now be obtained to create the Spotify playlist later.
Now that we have the songs collected from the Billboard website, we can search for them. Keep in mind that each music has a URI that we may use as a parameter when adding it to the Spotify playlist. Additionally, not all songs may be available on Spotify; thus, we must employ exception handling to skip such tracks. We can add those songs to the playlist using the sp object from the Spotify class.


