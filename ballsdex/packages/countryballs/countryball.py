import logging
import random
import string
from datetime import datetime

import discord

from ballsdex.core.models import Ball, Special, balls
from ballsdex.packages.countryballs.components import CatchView
from ballsdex.settings import settings

log = logging.getLogger("ballsdex.packages.countryballs")

spawnmsglist = [
    "Now, I'm no doctor... but you may be *slightly* addicted to this dex.",
    "Buy $KISSER today. We promise we won’t rug pull.", 
    "Look, A silly kisser appeared! Catch it before its silliness disappears!!! 🗣️",
    "I LOVE KISSERS!!!",
    "I worked hard on these messages! Just kidding... you can still catch this kisser though!",
    "This kisser is staring at you from afar.",
    "chat is this kisser going to be sniped",
    "Mods, catch this kisser 🌩️",
    "Convert to Kisserism.",
    "You should join the Kisserdex server... unless this is the Kisserdex server.",
    "Go give Lithium a MacedonKisser.",
    "I love this kisser in particular.",
    "Which one is it, you ask? Uhhhh... it's a kisser.",
    "Catch me to get kisses!",
    "They didn't believe in kissers... GOD DID",
    "This is kisser is tooooootally a T1. Trust me.",
    "TELL THEM TO BRING THE KISSERS OUT!",
    "Are you silly like this kisser below?",
    "Catch me! Layla feeds me very well.",
    "Catch me! Layla doesn't feed me too often.",
    "We love kissers here. Make sure you love kissers as much as we do.",
    "Ooooh you like catching kissers dont you?",
    "Catch me if you dare! >:3",
    "99% of Kisserdex players give up before they get a Fabled.",
    "This kisser is flipping insane.",
    "This kisser has a large sack of dabloons.",
    "I kissed a boy on November 17th 2022.",
    "I kissed a girl on November 17th 2022.",
    "Need help? Join our [Official Server](<https://discord.gg/kissers>)!",
    "Catch this kisser, and get a PS2 for free!",
    "This kisser plays Geometry Dash!",
    "Also try Icondex!",
    "Also try Ballsdex!",
    "Also try Pixeldex!",
    "Also try Musicdex!", 
    "Felt silly, might kiss someone later.",
    "Don't catch this kisser! (Reverse psychology works, right?)",
    "You see that kisser over there? It's fleeing!!! Get him!",
    "Jonas.",
    "This kisser sold me fent.",
    "This kisser is kinda gay ngl.",
    "This kisser forgot to take their amnesia medication.",
    "MUSTAAAAAAAAAAAAAAAAAAAAAAAAARD",
    "This kisser has gone to Chromakopia.",
    "KISSERRRRRRRRRRRRRRRRRRRRRRRRRRRS",
    "This kisser loves math... wait, was I supposed to say meth? Idk. I'm too high for this.",
    "are kissers edible",
    "W Farm Keep It Up",
    "i don't think kissers are edible",
    "Tell me why you think you deserve the greatest of all time, kisser lover!",
    "Can I pleaseeeeee get a waffle.",
    "I remember you was conflicted. Misusing your influence.",
    "It's not enough! Few solid kissers left, but it's not enough!",
    "This kisser LOVES gambling!",
    "owo! uwu! ewe! rawr!",
    "A kisser. Bottom Text.",
    "I forgor to write a message. 💀",
    "idk man just catch this",
    "︎ ",
    "This kisser started a riot against the government!",
    "This kisser will love you for eternity.",
    "This kisser MIGHT be in your walls.",
    "oh",
    "This kisser is NOT silly. Do not believe it.",
    "This kisser is wanted in 195 countries.",
    "jonasjonasjonasjonasjonasjonasjonasjonas",
    "i like green beans",
    "i hate green beans",
    "We don't repeat messages around these parts.",
    "This kisser was banned from the official Ballsdex server.",
    "i love kissing,,,,,,,, so much,,,,,,,,,,,,,,,",
    "🇸🇨",
    "I'm sure it's Bolivia.",
    "It must be Bolivia...",
    "This kisser is SEVERELY addicted to Kisserdex. Hopefully he will convert you.",
    "This kisser escaped from your local mental institution! Will you help them escape?",
    "Kisser, what's wrong? You look depressed! Do you not know what you are!? Or what your value is!?",
    "This message has a 1 in 20 million chance of appearing. No, we're kidding. Or are we? You'll never know.",
    "Every 60 seconds, a minute passes.",
    "Dude, I was fine with waiting 60 minutes for a kisser, but a whole hour!?",
    "This kisser said your home security is great. Or is it?",
    "Tetrahedral bonding makes water wet, as water sticks to water. Also, here's a kisser.",
    "Is it a kisser? Or just a figment of your imagination...",
    "I’m being held at gunpoint to keep spawning these. Don’t let my hard work go to waste.",
    "Just one more spawn... One more spawn and it'll be a mythic... Surely...",
    "when the",
    "Is the Spawn wave over?",
    "I HAVE A BOMB STRAPPED TO MY CHEST", 
    "Free Palestine. 🇵🇸",
    "Kissers can have a little salami... as a treat.",
    "HAVE YOU EVER PLAYED RUGBY ⁉️",
    "We were not able to afford this message. Consider supporting us on [Pawtreon](<https://www.patreon.com/kisserdex>).",
    "IN LIFE... ITS ROBLOX. DON'T LET NOTHING STOP YOU.",
    "A wild countryball spawned! Or was it an icon? A kisser perchance? We'll never know... not until you catch it!",
    "Keep farming I’m close",
    "Let's go gambling!!!",
    "(NEW METHOD) How to get FREE kissers in Kisserdex Discord Bot! (Working 2025) (Legit)",
    "<:tRaumatized:1243670211513548830>",
    "This kisser kisses kissers.",
    "Tell em Kendrick did it.",
    "She sells seashells sourced from Seychelles’ seashore.",
    "<a:alienpls:1260384104931786774>",
    "Stream GNX.",
    "Shoutout Icondex.",
    "All I ever wanted was a nice grand kisser! Drop being rational, give us what we asked for!",
    "This kisser is eating this text for no rea...",
    "Yesterday, somebody wacced out my kisser.",
    "Shoutout all my Kisserdex artists.",
    "Join our [Official Server](<https://discord.gg/kissers>) for free kissers. No, seriously. There’s giveaways like alllll the time.",
    "I'm running out of ideas on what to write here.",
    "As I recall, I know you love to show off... but I never thought you'd catch kissers through this all. What do I know?",
    "THERE'S AT LEAST A 1% CHANCE OF A BIG BIG GUMMY BEAR SPAWNING...",
    "that specific sensation accompanying the realisation that medical alterations to repair the patella bone will be occuring the following day",
    "All I want for christmas is a kisser!",
    "She don't believe in Kisserdex... but she believes in Kisser-flex...",
    "Your Text Here",
    "Custom Title",
    "This kisser knows exactly what it is. Do you?",
    "From the beer, to the keys, to the car, to the tree.",
    "She ain't ever met someone who talk like that, and when you hang up on that kisser, girl I call right back.",
    "Kisser.",
    "GET OUT 🗣️🔥💥",
    "This kisser is big. Massive even. We might be back.",
    "I bet 4 dollars and a gumball that you won't catch this kisser.",
    "those who know",
    "Catch this kisser, or double it and give it to the next person?",
    "those who grow: 🪴",
    "This kisser cannot afford a home due to inflation. Maybe you should catch them.",
    "catching this kisser will instantly kill you",
    "i hate rich people.",
    "This kisser is special, I think.",
    "I think you're forgetting that kissers only exist if you want them to. Why would you void them? That's rude.",
    "Go listen to A Wake In Providence.",
    "39 Buried. 0 Found.",
    "literally 1984",
    "DOWN WITH BIG KISSER!!!!!!!!!!!!!",
    "!ti hctaC !ressik a s'ti ,kooL",
    "I am so tired of spawning these. However, nobody will if I don't. I think we can all agree that no Kisserdex would be hell on earth.",
    "100% of things that breathe air end up dying. This means that air is the most lethal thing ever.",
    "<:petey:1291164562262982710>",
    "Look in my eyes, how could you NOT catch me?",
    "If you had 2 gummy worms. Would you. ?",
    "We are currently working on a new wave. It should be finished after GTA 6.",
    "If you haven't caught a Mythic, that's a skill issue.",
    "13 Raisins Why",
    "Kisserdex's RKK doesn't exist yet... maybe it will if you ask for it :3",
    "Here is a random sentence in Mandarin: 這個接吻者需要親吻.",
    "Here is a random sentence in Spanish: Este besador necesita besos.",
    "Here is a random sentence in English: This kisser needs kisses.",
    "Here is a random sentence in Hindi: इस चुम्बनकर्ता को चुम्बन की जरूरत है.",
    "Here is a random sentence in Bengali: এই চুম্বনকারীর চুম্বন দরকার.",
    "Here is a random sentence in Portuguese: Esse beijador precisa de beijos.",
    "Here is a random sentence in Russian: Этому целовальщику нужны поцелуи.",
    "Here is a random sentence in Japanese: このキス魔はキスを必要としている.",
    "It's dangerous to go alone. Take this.",
    "August 12, 2036, the heat death of Kisserdex.",
    "This kisser needs a place to stay!",
    "A wild silly kisser has appeared! Take care of it! <3",
    "A wild little kisser suddenly approaches you! Why don’t you pet it?!",
    "Kisserdex! Gotta catch em' all! *Wait. Is that copyrighted?*",
    "Look, it's a kisser! Catch it!",
    "Kisses for everyone!",
    "Catch me for a kiss!",
    "Look at this silly kisser!",
    "Kissers are the silliest!",
    "This kisser is ill! Only kisses will save them!",
    "im bored",
    "Wrong name!",
    "catch this kisser lil bro he doesn't feed himself",
    "Fun fact: kissers love milk, because it's actually an abbreviation that means Man I Love Kissing.",
    "A wild kisser has spawned! (Catch it now or be shot)",
    "Catch this kisser or it will switch your keyboard to a different language.",
    "I came, I saw, I kissed.",
    "A smooth sea never made a skilled sailor, but smooth kisses have definitely made skilled kissers.",
    "Kiss. Now.",
    "you would not believe your eyes if ten million kissers lit up this server as you fell asleep",
    "Hold me, kiss me!",
    "This here, is Cundalini. And Cundalini wants his paw back.",
    "Super silly kissers in your area. Tap to continue.",
    "Getting verified was a sisyphean task.",
    "OGs remember when Kisserdex wasn't verified.",
    "This kisser will die historic on Fury Road!"
    "WHAT A DAY! WHAT A LOVELY DAY!",
    "So shiny, so chrome.",
    "Where do we go, we who wander this wasteland in search of our better selves?",
    "Who killed the world?", "AGHHHHHH! I hate guns.", "It is by my paw you will rise from the ashes of this world.", "Sing, kissers! Sing! Siiiiing!!!", "I am the Nightkisser! I am a fuel-injected silliness machine! I am a rockah! I am a rollah! I am an out of controllahhhhhhhhh!!!", "Push me, shove you?", "Oh yeah, says who?", "This kisser is about to eat the sun.", "She tells me stories, she tells me tales.", "Here's the truth of the matter. No masks, no games.", "Up the mystic tower high, relinquish your mind.", "Kisser-tales are not found, they are written in the walls.", "The laws of the land or the heart, what's greater?", "WELCOME TO THE NEW AGE.", "It's useless, I've kissed to no avail.", "Bats can be pollinators & indicators of a healthy ecosystem.", "There's a 102% chance Layla and Cancat are yapping right now.", "Chat was this spawn natural?", ":3", "Try entering Kisserdex, it's the correct answer.", "fish react the person above me 🐟", "Why So Kisserdex?", "What if we caught this one?", "Could I get some ketchup on the side with this one, please?", "No, you can't add me to 50 farm servers!", "What do you mean you don't have 100% comp yet?", "Collect my Messages...", "😂 This is a fake spawn by the way.", "Hurry, catch it before it flies into pig_man77's orbit!", "Look, it says gullible on the ceiling!", "Hold on, I think we took a wrong turn...", "There's a Vietnam countrie kisser and I keep saying Vietnam but kissert decks. Keep saying that it's wrong.", "Hello Vro ♥️", "It's farming time!", "(*Accidentally blacklists you*) Oops, guess you can't catch it anymore...", "Go to bed already!", "<:rahhhh:1208044649260908604> GIVE ME FENT!", "If I roll a 12, you have to catch this kisser.", "It ain't even noon and I've got kissing on my mind.", "DONT TRUST LAYLA SHES EVIL THIS BOT IS A SETUP", "This kisser has absolutely NO disorders at all!", "This kisser farms Kisserdex players.", "This kisser's name ISN'T meow.", "Just because we're in an impoverished world, it doesn't mean people stop making beautiful things.", "As the world falls around us, how must we brave its cruelties?", "Kisserdex is a lie made up by the CIA.", "Catch me while the economy is still stable.", "What economy? Catch this to make it worse.", "My economy is worse than Weimar's in 1923.", "<:laylers:1211077571400171540>", "This kisser was brought to you by our awesome artists.", "Hey guys, Kisserdex here... this is my official face reveal!", "how it feels to catch kissers in kisserdex", "This kisser burnt down 53 orphanages in 1967!", "Catch this kisser. No buts. Catch it.", "This kisser will be sniped within 5 seconds by daniekvanlee.", "It was at this point in time where I realized I needed to switch schools just to catch kissers.", "homecoming - slice the cake", "Help me catch this kisser!", "I just got out of the backrooms.", "Mwah! The kisser kissed you, catch it before it can kiss others!", "Bukiry will take this kisser, don’t touch it.", "The weather today is good. ☀️", "This kisser is on a kissing spree!", "Is it a bird? Is it a plane? No, it's a kisser sliding into your inventory.", "How much kissers could a silly kisser kiss if a silly kisser could kiss kissers?", "KISSERDEX IS MY LIFE", "What is the purpose of life? Kisserdex of course.", "Feeling lucky? There’s a 1 in 2048 chance this kisser is a shiny!", "This kisser might go insane at any moment.", "100% of experts recommend playing Kisserdex to cure your boredom.", "This kisser can be trusted with nuclear launch codes.", "9 out of 10 dentists recommend catching this kisser!", "The tenth dentist is Layla.", "<:boykisser:1157162763995586590>", "The US government demands your Kazakhstans.", "Do you want this silly kisser to steal all your personal information? If not, then you should download Nord VP-", "This message was sponsored by Raid Shadow Lege-", "pluh", "Sometimes I wonder what I'm gonna do, 'cause there ain't no cure for the Kisserdex blues.", "They say people don't believe in kissers anymore. Well damn them! You and me, goober, we're gonna give them back their kissers!", "kisserdex when the dex kisses me idk never played the game", "The chain in those pawcuffs is high-tensile steel. It'd take you ten minutes to hack through it with this. Go!", "GUN FEVERRRRR!!!!", "Just one angry shot for Furiosa!", "The stars be with you.", "Kiss me, compete, dream bad at night, repeat.", "I could really go for a Hautdog right now.", "Forward! Forget your fear, the kissers at your back scream forward!", "Perhaps this was the result of an anxiety.", "Are We Fit for Glory Yet? (The Kiss to End Nothing)", "Just. Walk. Away.", "Political.", "All of this for a kisser squabble.", "Real evolutionary, evidentiary backup.", "I got silly issues, that's on me.", "All you have, all you are, is silliness.", "You may be raw, but you have about you a purposeful savagery.", "Remember me?", "This is our first fruit, but it's not for you and me. Each of us, in our own way, will vanish from this earth. And then, pawhaps... some uncorrupted life will rise to adore them.", "Let him come. Body search, no weapons. Whatever he wants, we'll listen. Then kiss him on the spot.", "This kisser is looking for a place of abundance!", "Is this Valhalla?", "Catch this kisser. Now? Now!!!", "This is the darkest of angels. The fifth rider of the apocalypse.", "Question is, do you have it in ya to make it epic?", "This kisser drives a Chevrolet movie theatre.", "What the kisser? What that mean?", "Meow, get out the way.", "I may be evil and I may be vile, but you must be silly, 'cause I made you smile.", "This kisser has been in every buc-ee's in the USA!", "I Might Be Stealing Your Personal Information", "Once you're in, there's no way out.", "this silly lil guy wants to give you a pipebomb :3", "Kissers are temporary, but doom is eternal. Catch this kisser before doom swallows it whole.", "kiss, kiss, kiss.", "This kisser has invaded the server! Catch it quick to regain your territory.", "every 60 spawns in kisserdex, a minute passes (layla spawned 59 of them)", "Legend has it Layla took one look at an economy class and immediately dropped out to start Kisserdex.", "<:boykisser_down:1320793371844804701>", "The first rule of Kisser Club is you do not yap about Kisser Club.", "Keep missing spawn waves? Consider supporting us on [Pawtreon](<https://www.patreon.com/kisserdex>) to get infinite spawn waves delivered to your home <:speaking_kisser:1320527175333707926>", "Are you unable to catch kissers? Maybe you should try some speed typing challenges.", "This message is deeply political. Be enraged.", "32g of protein", "farmfarmfarm", "meow :3", "What's your favorite song?", "Who's your favorite band?", "If you could be anywhere in the world, what location would you choose?", "This kisser loves the Oxford Comma.", "THE KISSER! THE KISSER IS REAL!", "This Kisser is ballin’.", "A domesticated kisser appeared!", "The kiss to end all kisses.", "Just chase the next high... I mean kisser.", "I HAVE CAUGHT THESE KISSERS BEFORE!", "This kisser supports the universal right to kiss.", "thshshyhdshyhruiofdhgyr46euhdgterbthyujygtfrndberty7ugtfrdgegthyujnygtfrhyjuygtfvyh", "why do they call it kisserdex when you of in the cute kisser of out caught kiss the kisser", "To kiss or to be kissed?", "Forfeit all mortal possessions to this fella.", "It doesn't matter if you're gay, straight or bisexual. At the end of the day, it's night.", "2012, go ask the Mayans.", "10 Reason why Kisserdex is the best:", "Hi Did You Guys Know That Farming Is Legal In Kisser Dex", "im thinkig weawwy weawwy hawddd,,,", "There is at least 1 reason to catch this kisser. I'm not gonna tell you what it is.", "rawr XD", "WAS THAT THE SPAWN WAVE OF 87'", "This Kisser Is Never Gonna Give You Up", "Brought to you by mastermind George Miller!", "George Orwell would've loved Kisserdex.", "Wave 100 when??", "did you know that happy feet and mad max are directed by the same guy", "This is a **new kisser** that.. Uhh… Sorry, too early!", "god giveth", "and god taketh away", "This kisser walked up to your lemonade stand.", "A law banning Kisserdex has been enacted in the United States. Unfortunately, that means you can’t use Kisserdex for now.", "this kisser is green", "Congratulations <@1144609173879918603>! You have reached **level ∞**! 🎉"]

class CountryBall:
    def __init__(self, model: Ball):
        self.name = model.country
        self.model = model
        self.algo: str | None = None
        self.message: discord.Message = discord.utils.MISSING
        self.catched = False
        self.time = datetime.now()
        self.special: Special | None = None
        self.atk_bonus: int | None = None
        self.hp_bonus: int | None = None

    @classmethod
    async def get_random(cls):
        countryballs = list(filter(lambda m: m.enabled, balls.values()))
        if not countryballs:
            raise RuntimeError("No ball to spawn")
        rarities = [x.rarity for x in countryballs]
        cb = random.choices(population=countryballs, weights=rarities, k=1)[0]
        return cls(cb)

    async def spawn(self, channel: discord.TextChannel) -> bool:
        """
        Spawn a countryball in a channel.

        Parameters
        ----------
        channel: discord.TextChannel
            The channel where to spawn the countryball. Must have permission to send messages
            and upload files as a bot (not through interactions).

        Returns
        -------
        bool
            `True` if the operation succeeded, otherwise `False`. An error will be displayed
            in the logs if that's the case.
        """

        def generate_random_name():
            source = string.ascii_uppercase + string.ascii_lowercase + string.ascii_letters
            return "".join(random.choices(source, k=15))

        extension = self.model.wild_card.split(".")[-1]
        file_location = "./admin_panel/media/" + self.model.wild_card
        file_name = f"nt_{generate_random_name()}.{extension}"
        try:
            permissions = channel.permissions_for(channel.guild.me)
            if permissions.attach_files and permissions.send_messages:
                self.message = await channel.send((random.choice(spawnmsglist)),
                    view=CatchView(self),
                    file=discord.File(file_location, filename=file_name),
                )
                return True
            else:
                log.error("Missing permission to spawn ball in channel %s.", channel)
        except discord.Forbidden:
            log.error(f"Missing permission to spawn ball in channel {channel}.")
        except discord.HTTPException:
            log.error("Failed to spawn ball", exc_info=True)
        return False
