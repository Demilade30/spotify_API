## Working with Spotify API

*This code retrieves album information from Spotify*

This project highlights the use of APIs, SDKs, and Libraries

Whenever you run this code with required input, album/ track information is outputted from [Spotify API](https://developer.spotify.com/)

### How does it work?

User inputs the album/ track information and they are able to see specific information about the song/ list of songs.

```markdown
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import spotipy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "clientId = 'faeecd78395c4018a27b724b85c94c9f'\n",
    "clientSecret = 'eb655fc8edaa463a8f4f9fd464e4641e'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "authUrl = 'https://accounts.spotify.com/api/token'\n",
    "auth_response = requests.post(authUrl, {\n",
    "    'grant_type' : 'client_credentials',\n",
    "    'client_id' : clientId,\n",
    "    'client_secret' : clientSecret,\n",
    "})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "200\n"
     ]
    }
   ],
   "source": [
    "print(auth_response.status_code)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "auth_responseData = auth_response.json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'access_token': 'BQC2HKPm1t4hKvMrH3B78NJVe5Hv0ZAkBnTvAKjnzyUdAT4SPMmXyS-EQeOS5VPrc2gjIcwtLijDsiw7vVs',\n",
       " 'expires_in': 3600,\n",
       " 'token_type': 'Bearer'}"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "auth_responseData"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "accessToken = auth_responseData"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "headers = {\n",
    "    'Authorization': 'Bearer {token}'.format(token=accessToken)\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "baseUrl = 'https://api.spotify.com/v1/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "trackId = '6mFkJmJqdDVQ1REhVfGgd1'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "r = requests.get(baseUrl + 'audio-features/' + trackId, headers=headers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

```
Elon Musk:
> "When something is important enough, you do it even if the odds are not in your favor."

# Installation
* Runs on python 2.7>
* Run command "sudo pip3 install spotipy" to begin

## Contributors
[Click here to learn more](https://github.com/Demilade30)

### License

- [GNU GPL](license)
- ![badge0](https://img.shields.io/static/v1?label=<License>&message=GNU>&color=<BLUE>)

### **Special thanks to:**
1. _Nikhil Yadav_
2. _Jean Emile Leconte II_

### On behalf of SEO Tech Developer

![https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.seo-usa.org%2Fwp-content%2Fuploads%2F2019%2F01%2Fseo-logo-og.png&imgrefurl=https%3A%2F%2Fwww.seo-usa.org%2F&tbnid=YiZddZtBXxH6AM&vet=12ahUKEwjAiJCP3eLxAhXTbqwKHUKBDk8QMygAegUIARCoAQ..i&docid=JkiQ-7yjC_4A7M&w=1200&h=627&q=seo-usa&ved=2ahUKEwjAiJCP3eLxAhXTbqwKHUKBDk8QMygAegUIARCoAQ](src)
For more details see [SEO Tech Deveoloper](https://www.seo-usa.org/career/tech/).

# About:
* Divine Demilade Akinjiyan
* Junior, Double majoring in Math and Computer Science
* [LinkedIn](https://www.linkedin.com/in/divine-akinjiyan/).
* [Github](https://github.com/Demilade30) or [Email](divine.akinjiyan@gmail.com).
