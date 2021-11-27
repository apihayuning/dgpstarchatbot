import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Update, ReplyKeyboardRemove, ForceReply
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters

from flask import Flask
import asyncio

loop = asyncio.get_event_loop()
app = Flask(__name__)

@app.route('/')
def index():
    
    # keyboard
    how_is_work = [
        [InlineKeyboardButton("✅ Set up your wallet", callback_data='how_is_work01'), InlineKeyboardButton("✅ Create your collection", callback_data='how_is_work02')],
        [InlineKeyboardButton("✅ Add your NFTs", callback_data='how_is_work03'), InlineKeyboardButton("✅ List them for sale", callback_data='how_is_work04')]
    ]

    collection_key = [
        [InlineKeyboardButton("➡️ Click Here", url='https://dgpstar.com')]
    ]

    troubleshooting_key = [
        [InlineKeyboardButton("❓ Troubleshooting help", url='https://www.youtube.com/watch?v=8Pq3ohFwaPE')]
    ]

    community_key = [
        [InlineKeyboardButton("📢 Telegram", url="https://t.me/dgpstarnft")],
        [InlineKeyboardButton("📢 Instagram", url="https://www.instagram.com/dgp.star"),
        InlineKeyboardButton("📢 YouTube", url="https://www.youtube.com/channel/UChqA4yVKavxnu08TssLhzhg")]
    ]

    faq_key = [
        [InlineKeyboardButton("⚠️ NFT? ERC-721 tokens?", callback_data="faq_01")],
        [InlineKeyboardButton("⚠️ What does “minting” mean?", callback_data="faq_02")],
        [InlineKeyboardButton("⚠️ Can I create an NFT on DGPSTAR.COM without putting it on sale?", callback_data="faq_03")],
        [InlineKeyboardButton("⚠️ Can I change the price of an already created collectible?", callback_data="faq_04")],
        [InlineKeyboardButton("⚠️ Can I gift or send a collectible to someone?", callback_data="faq_05")],
        [InlineKeyboardButton("⚠️ What does “burn a token” mean?", callback_data="faq_06")],
        [InlineKeyboardButton("⚠️ Do you have an OpenSea integration?", callback_data="faq_07")],
        [InlineKeyboardButton("⚠️ What is the purpose of $DGP as a governance token?", callback_data="faq_08")],
        [InlineKeyboardButton("⚠️ What is “unlockable content”?", callback_data="faq_09")],
        [InlineKeyboardButton("⚠️ How does the royalty system work?", callback_data="faq_10")],
        [InlineKeyboardButton("⚠️ I would like to suggest additional features!", callback_data="faq_11")],
        [InlineKeyboardButton("⚠️ Can I report an artwork or collectible?", callback_data="faq_12")],
        [InlineKeyboardButton("⚠️ What is verification?", callback_data="faq_13")],
        [InlineKeyboardButton("⚠️ How to get a “verified” badge?", callback_data="faq_14")],
        [InlineKeyboardButton("⚠️ It's been a while and I don't get verified. Why?", callback_data="faq_15")]
    ]

    def start(update: Update, context: CallbackContext) -> None:
        """Sends a message with three inline buttons attached."""
        query = update.callback_query

        def openKeyboard():
            rkeyboard = [
                [KeyboardButton('ℹ️ About Us')],
                [KeyboardButton('❓ What is NFT'), KeyboardButton('❓ How is work')],
                [KeyboardButton('💬 FAQs'), KeyboardButton('👥 Community'), KeyboardButton('📚 Collection')]
                # [KeyboardButton('📶 How is work'), KeyboardButton('🛠 Setting DGPBOT')],
                # [KeyboardButton('♻️ Create Binance Account')],
                # [KeyboardButton('♻️ Join DGPBot'), KeyboardButton('💬 FAQ')],
                # [KeyboardButton('❓ Troubleshooting help')],
                # [KeyboardButton('🎯 Thoughts and Advices')]
            ]

            reply_kmarkup = ReplyKeyboardMarkup(rkeyboard)
            update.message.reply_text(text='🌟 *Welcome to our Service* 🌟', reply_markup=reply_kmarkup, parse_mode=telegram.ParseMode.MARKDOWN)
        
        if '/start' == update.message.text:
            openKeyboard()

        # reply_markup = InlineKeyboardMarkup(keyboard)
        # update.message.reply_text('Main Menu', reply_markup=reply_markup)

    def button(update: Update, context: CallbackContext) -> None:
        """Parses the CallbackQuery and updates the message text."""

        query = update.callback_query
        query.answer()

        # how_is_work
        if 'how_is_work01' == query.data:
            query.message.reply_text(text="<b>Set up your wallet</b>\n\nOnce you’ve set up your wallet of choice, connect it to DGPSTAR by clicking the wallet icon in the top right corner. Metamask is first our wallet support.", parse_mode=telegram.ParseMode.HTML)
            
        elif 'how_is_work02' == query.data:
            query.message.reply_text(text="<b>Create your collection</b>\n\nClick Create and set up your collection. Add social links, a description, profile & banner images, and set a secondary sales fee.", parse_mode=telegram.ParseMode.HTML)
        
        elif 'how_is_work03' == query.data:
            query.message.reply_text(text="<b>Add your NFTs</b>\n\nUpload your work (image, video, audio, or 3D art), add a title and description, and customize your NFTs with properties, stats, and unlockable content.", parse_mode=telegram.ParseMode.HTML)

        elif 'how_is_work04' == query.data:
            query.message.reply_text(text="<b>List them for sale</b>\n\nChoose between auctions, fixed-price listings, and declining-price listings. You choose how you want to sell your NFTs, and we help you sell them!", parse_mode=telegram.ParseMode.HTML)
            
        elif 'dca_set_re_buy' == query.data:
            query.message.reply_text(text="<b>How to Dollar-Cost Averaging (DCA), Set Re-buy</b>\n\nThis means that if you are in a signal and price drops, bot will automatically rebuy the coin to lower your average buy price. Dollar-Cost averaging is a really helpful method to exit the signal as early as possible. However, it should be noted that this might also get you in a position with huge loss. Decide carefully how many times to buyback again.\n\n<b>→ Settings → Re-buy → Click how many times you want to re-buy.</b>", parse_mode=telegram.ParseMode.HTML)

        elif 'percentage' == query.data:
            query.message.reply_text(text="<b>How to Set Re-buy Percentage</b>\n\nTo apply Dollar-Cost Averaging, you must define a distance to have the bot buy again for you.\n\n<b>Let’s examine this situation:</b>\nYour re-buy % = 3%\nYou bought a signal when it is 10000 satoshi, it means that your first re-buy will be when price is 9700 satoshi.\nYour second re-buy will be when price is 9700*0.97=9409 satoshi\nYour third re-buy will be when price is 9409*0.97=9127 satoshi\n\n<b>→ Settings → Stop Loss → Click what percentage do you want to set.</b>", parse_mode=telegram.ParseMode.HTML)

        elif 'deactivate_sl' == query.data:
            query.message.reply_text(text="<b>How to Set/Deactivate Stop-loss</b>\n\nStop-loss can be defined as an advance order to sell an asset when it reaches a particular price point. It is used to limit loss or gain in a trade. By placing a stop-loss order, the investor instructs the broker/agent to sell a security when it reaches a pre-set price limit\n\n<b>→ Settings → Stop Loss → Click what percentage do you want to set.</b>\n\n<b>Note:</b> If you don't want to set stop-loss, click Don't use stop loss", parse_mode=telegram.ParseMode.HTML)

        elif 'maximum_signal' == query.data:
            query.message.reply_text(text="<b>How to Set Maximum Signal</b>\n\nIn order to use your budget effectively and apply dollar-cost averaging, you should adjust the maximum number of signals you will be trading at the same time.\n\n<b>→ Settings → Max Signal → Click how many signals you want to trade at the same time.</b>", parse_mode=telegram.ParseMode.HTML)

        elif 'cancel_order' == query.data:
            query.message.reply_text(text="<b>How to Set Cancel Order Time</b>\n\nIn some cases, the signal may be completed before the orders we placed are filled, and the order may remain open for no reason. Therefore, it would be in our best interest to cancel our orders automatically after a certain period of time.\n\n<b>→ Settings → Cancel Order → Click how many minutes you want to wait before canceling the order.</b>", parse_mode=telegram.ParseMode.HTML)

        elif 'trail_stop' == query.data:
            query.message.reply_text(text="<b>How to Set Trail Stop</b>\n\nThis feature is under construction currently. It will be documented later.", parse_mode=telegram.ParseMode.HTML)

        elif 'algorithm' == query.data:
            query.message.reply_text(text="<b>How to Activate/Deactivate an Algorithm</b>\n\nSimply click on the algorithm you want to activate/deactivate.", parse_mode=telegram.ParseMode.HTML)
            query.message.reply_photo(photo="https://blogger.googleusercontent.com/img/a/AVvXsEieRAKrJ-7k8K2PlE7Lp3f83EBujIGtCAKdl6fwHwRpa831jCdNviissyL0hjNN0OVQnfYphX7DqPO-kG_z2-iYs9qRRYq-SkLdSx3oShEc5H_NXJMgYEGKusjdoA-2iVVs83GxjuKKLaNMaMKl1VjRTvvNsi7onQZfEJfMaRTb-g1qdmRhG8JKWE6tIg=s339")

        # FAQ 

        elif 'faq_01' == query.data:
            query.message.reply_text(text="<b>NFT? ERC-721 tokens</b> ❓\n\nNFT stands for non-fungible tokens like ERC-721 (a smart contract standard) tokens which are hosted on Ethereum’s own blockchain. NFTs are unique digital items such as collectibles or artworks or game items. As an artist, by tokenizing your work you both ensure that it is unique and brand it as your work. The actual ownership is blockchain-managed.\nIf you want to go in-depth into NFTs, I suggest this read: https://", parse_mode=telegram.ParseMode.HTML)

        elif 'faq_02' == query.data:
            query.message.reply_text(text="<b>What does “minting” mean</b> ❓\n\nThe process of tokenizing your work and creating an NFT (see above).", parse_mode=telegram.ParseMode.HTML)

        elif 'faq_03' == query.data:
            query.message.reply_text(text="<b>Can I create an NFT on DGPSTAR without putting it on sale</b> ❓\n\nYes, you can and it is up to you if you decide to sell it later or not.", parse_mode=telegram.ParseMode.HTML)

        elif 'faq_04' == query.data:
            query.message.reply_text(text="<b>Can I change the price of an already created collectible</b> ❓\n\nAbsolutely, you can lower the price free of transaction costs at any time. You just need to sign the signature request via your wallet.", parse_mode=telegram.ParseMode.HTML)

        elif 'faq_05' == query.data:
            query.message.reply_text(text="<b>Can I gift or send a collectible to someone</b> ❓\n\nYes, just go on the detail page of a collectible you own, open the “...” menu and select “transfer token”", parse_mode=telegram.ParseMode.HTML)

        elif 'faq_06' == query.data:
            query.message.reply_text(text="<b>What does “burn a token” mean</b> ❓\n\nThe ERC-721 standard does not only allow the creation of NFTs, but also includes a possibility to destroy them - i.e. burning the token.", parse_mode=telegram.ParseMode.HTML)

        elif 'faq_07' == query.data:
            query.message.reply_text(text="<b>Do you have an OpenSea integration</b> ❓\n\nYes, you can view the collectibles you have created on DGPSTAR.COM on OpenSea and manage them there as well. Additionally, it is possible to list your collectibles on OpenSea not only in WETH but also in $DGP.", parse_mode=telegram.ParseMode.HTML)

        elif 'faq_08' == query.data:
            query.message.reply_text(text="<b>What is the purpose of $DGP as a governance token</b> ❓\n\nPlease refer to this article: https://", parse_mode=telegram.ParseMode.HTML)

        elif 'faq_09' == query.data:
            query.message.reply_text(text="<b>What is “unlockable content”</b> ❓\n\nAs a content creator, you can add unlockable content to your collectibles, that only becomes visible after a transfer of ownership (i.e. selling or gifting your NFT). Artists use this feature to include high res files, making ofs. videos, secret messages etc.", parse_mode=telegram.ParseMode.HTML)

        elif 'faq_10' == query.data:
            query.message.reply_text(text="<b>How does the royalty system work</b> ❓\n\nWhenever you create a collectible you can set a certain percentage as royalty for secondary sales. Example: You create a digital painting and sell it for 0.2 ETH, the royalty is 10 percent. Your buyer then sells your painting at a higher price point for 0.5 ETH. Here, the royalty system kicks in. As the original content creator you receive 10% of that sale, being 0.05 ETH.\n\n<b>NB:</b> Royalties set on OpenSea don’t carry over to DGPSTAR.COMat the moment. However, the team is working on a cross-platform royalities implementation.", parse_mode=telegram.ParseMode.HTML)

        elif 'faq_11' == query.data:
            query.message.reply_text(text="<b>I would like to suggest additional features</b> ❓\n\nYou can do this here: https://", parse_mode=telegram.ParseMode.HTML)

        elif 'faq_12' == query.data:
            query.message.reply_text(text="<b>Can I report an artwork or collectible</b> ❓\n\nYes, go on the detail page of the token you want to report, click on the “...” button and select “Report”.", parse_mode=telegram.ParseMode.HTML)

        elif 'faq_13' == query.data:
            query.message.reply_text(text="<b>What is verification</b> ❓\n\nVerified badges are granted to creators and collectors that show enough proof of authenticity and active dedication to the marketplace. We are looking at multiple factors such as active social media presence and following, dialogue with community members,number of minted and sold items.", parse_mode=telegram.ParseMode.HTML)

        elif 'faq_14' == query.data:
            query.message.reply_text(text="<b>How to get a “verified” badge</b> ❓\n\nThe only way to get verified is to fill out this form.\nHere are some tips on getting it right.\nYou need to submit:\n\n✅ Filled-in profile on DGPSTAR: user pic + cover + custom link\n\n✅ Links to at least 2 social media profiles What we're looking for is active social media presence with a history, sharing your artworks, participating in the community. Large followers base is a plus. Mass-following raises questions.\n\n✅ Behind the screens/work in progress If you're a creator, show us the backstage of the work process on one of the minted items. If you’re a collector and it's not applicable, we will take a look at the items you previously purchased.\n\n✅ The story behind your account Tell us about yourself! Why are you on DGP TOKEN? What are you selling/collecting? What is the concept of your art?\n\n<b>note:</b> Read our full guide to getting verified.", parse_mode=telegram.ParseMode.HTML)

        elif 'faq_15' == query.data:
            query.message.reply_text(text="<b>It's been a while and I don't get verified. Why</b> ❓\n\nIf you're not verified within a week since submitting your request, most likely you didn't provide enough information, or your DGP TOKEN account is not active enough.\nPlease note that the team reserves the right to not grant the verified badges without further explanation, as we receive hundreds of requests on a daily basis.\nHowever, don't let it discourage you! The verified badge is not the key to success on the marketplace. Fill in your profiles, make more sales or purchases, and try one more time later.\nGood luck!", parse_mode=telegram.ParseMode.HTML)

    def mainButton(update: Update, context: CallbackContext) -> None:

        if 'Main Menu' == update.message.text:
            # update.message.delete(10)
            rem_kmarkup = ReplyKeyboardRemove(True)
            update.message.reply_text('Main Menu', reply_markup=rem_kmarkup)

            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text('Main Menu', reply_markup=reply_markup)

        elif 'ℹ️ About Us' == update.message.text:
            # update.message.delete(10)
            update.message.reply_text('♻️ <b>About Us</b> ♻️\n\n✅ DGPSTAR is peer-to-peer marketplace for cryptogoods, digital art, original certificate and rare items, which include collectibles, gaming items, and other virtual goods backed by a blockchain. On DGPSTAR, anyone can buy or sell these items through a smart contract\n\n✅ The platform allows the digital representation of unique assets in the form of NFTs with the standards of Ethereum that offer substantial benefits and a huge reputation from the global market for NFTs. This art-centric marketplace has a huge reputation for arts and artists that receives global recognition from the creators and NFT collectors.\n\n✅ Our market place allows us to create, sell and bid for NFTs which also allows purchasing NFTs from other marketplaces. Our plethora of NFTs in our marketplace offers a better investment opportunity for digital assets that offer enormous crypto fortunes as rewards for financial freedom.', parse_mode=telegram.ParseMode.HTML)

        elif '❓ What is NFT' == update.message.text:
            # update.message.delete(10)
            update.message.reply_text("♻️ <b>What is NFT</b> ♻️\n\n<i><b>A Non-Fungible Token (NFT)</b> is a unique digital asset that represents ownership of real-world items like art, video clips, music, and more. NFTs use the same blockchain technology that powers cryptocurrencies, but they're not a currency.</i>", parse_mode=telegram.ParseMode.HTML)
        
        elif '❓ How is work' == update.message.text:
            # update.message.delete(10)
            reply_markup = InlineKeyboardMarkup(how_is_work)
            update.message.reply_text('♻️ <b>Create and sell your NFTs</b> ♻️', reply_markup=reply_markup, parse_mode=telegram.ParseMode.HTML)

        elif '♻️ Join DGPBot' == update.message.text:
            # update.message.delete(10)
            reply_markup = InlineKeyboardMarkup(registerdgpbot_key)
            update.message.reply_text('♻️ Join DGPBot ♻️', reply_markup=reply_markup)

        elif '❓ Troubleshooting help' == update.message.text:
            # update.message.delete(10)
            reply_markup = InlineKeyboardMarkup(troubleshooting_key)
            update.message.reply_text('♻️ Troubleshooting help ♻️', reply_markup=reply_markup)

        elif '👥 Community' == update.message.text:
            # update.message.delete(10)
            reply_markup = InlineKeyboardMarkup(community_key)
            update.message.reply_text('♻️ <b>Community</b> ♻️', parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)

        elif '💬 FAQs' == update.message.text:
            # update.message.delete(10)
            reply_markup = InlineKeyboardMarkup(faq_key)
            update.message.reply_text('♻️ <b>Frequently Asked Questions</b> ♻️', parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)

        elif '📚 Collection' == update.message.text:
            reply_markup = InlineKeyboardMarkup(collection_key)
            update.message.reply_text('♻️ <b>DgpStarNFT Collection</b> ♻️', parse_mode=telegram.ParseMode.HTML, reply_markup=reply_markup)

    async def main():
        updater = Updater("2093633654:AAGOU-gY23RXNfQfDS88I2s6GRLGL4n4vrA", request_kwargs={'read_timeout': 6, 'connect_timeout': 7})
        
        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(CallbackQueryHandler(button))
        updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), mainButton))
        
        updater.start_polling()

    loop.run_until_complete(main())

    return "success.."