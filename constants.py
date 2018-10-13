token = '572637496:AAEitWigXlgKarpFgOp_d_wUWVv5RcpYpJo'

hello_text = '''Привет! В данном боте мы предлагаем заключить тебе пари и угадать, куда пойдёт курс криптовалют «вниз» или «вверх».

Если ты будешь прав мы начислим тебе 80% от твоей ставки.

К примеру ты поставил 1 BTC и верно угадал направление, в таком случае мы выплатим тебе 1,8 BTC, при этом курс мог изменится даже на 1$ в нужном тебе направлении.

Период ставки можно выбирать самому, всего 6 вариантов

Удачных тебе пари!'''

admin = 286077227

admin2 = 673974337

valume = ''

hey_text = ['Чем могу помочь?', "Доброго времени суток!",  "И чем же мы сейчас займемся?", "Здравствуйте!"]

hey_text_e = ['And what are we going to do now?', 'How can I help?', 'Hello!']

kurs = '''Состояние курса монет на данный момент:
BTC/USD - %s
ETH/USD - %s
XRP/USD - %s
BCH/USD - %s
EOS/USD - %s
LTC/USD - %s

Вы можете сделать ставку на то, что будет курс выше или ниже.'''

btc_text_e = '''
To replenish BTC from an external wallet, use the one-time address below.
(amount not less than 0,001 BTC)'''



FAQ = '''-В чем смысл вашего бота?
-Наш бот  предлагает вам угадать, куда пойдет курс Биткоина, вверх или вниз, другими словами заключить пари. Вы сами выбираете время и пару. 

Когда вы заключили сделку, икогда наступает расчетное время, и если вы верно угадали направление курса, вам начисляется 80% прибыли от суммы вашей ставки.


-Пари проводятся каждый день?
-Да, пари проводятся круглосуточно, каждый день.


-С какого источника берётся курс Биткоина?
-Курс автоматически берётся с https://coinmarketcap.com/


-Как пополнить баланс в вашем боте?
-Выберете кнопку «Пополнить баланс», далее выберите способ пополнения Bitcoin(BTC), Ethereum(ETH) или ЯД (Яндекс Деньги)

Переведите на указанный кошелёк сумму и нажмите Оплатил. 
Как только вы нажмете Оплатил, система автоматически зачислит на ваш баланс средства после 1-го подтверждения сети.


-Какая минимальная сумма пополнения?
-Для Bitcoin 0,001 BTC. Для Ethereum 0,02 ETH. 
Для Яндекс денег 1000 рублей.


-Какая минимальная сумма пари?
-Минимальная сумма пари 0,001 BTC. 



-Я пополнил баланс бота в Ethereum или Яндекс Деньги, вы автоматически сконвертируете его в Bitcoin?
-Да, баланс бота подсчитывается в Bitcoin(BTC). При пополнении баланса в Ethereum(ETH), мы автоматически сконвертируем его в BTC.


-Как я могу вывести средства?
1. Нажмите в боте кнопку «Вывести средства»
2. Выберите Bitcoin(BTC), Ethereum(ETH) или Яндекс Деньги (Yandex Money) 
3. Введите адрес вашего кошелька
4. Введите сумму для вывода


-Есть ли у вас реферальная система?
-Да, у нас присутствует реферальная система. Свою реферальную ссылку вы можете найти нажав кнопку «Дополнительно», далее «Рефералы». 

За каждого человека, кто перейдёт по вашей ссылке и внесёт депозит, мы выплачиваем 0,0005 BTC(~1$)


Спасибо, что ежедневно участвуете в наших пари!'''

FAQ_2 = '''-What is the meaning of your bot?
-Our bot offers you to guess where Bitcoin will go, up or down, in other words to make a bet. You choose the time and the pair.

When you have made a deal, when the estimated time comes, and if you correctly guessed the direction of the course, you earn 80% of the profit on the amount of your bet.


-Pairs are held every day?
Yes, the betting is done around the clock, every day.


- What is the source of the Bitcoin course?
-Course is automatically taken from https://coinmarketcap.com/


-How to replenish the balance in your bot?
- Choose the button “Top up the balance”, then select the method of replenishing Bitcoin (BTC), Ethereum (ETH) or POISON (Yandex Money)

Transfer to the specified wallet amount and click Pay.
As soon as you click on Pay, the system will automatically credit the funds to your balance after the 1st confirmation of the network.


-What is the minimum amount of replenishment?
-For Bitcoin 0.001 BTC. For Ethereum 0.02 ETH.
For Yandex money 1000 rubles.


-What is the minimum wager amount?
- The minimum bet amount is 0.001 BTC.



-I filled up the balance of the bot in Ethereum or Yandex Money, do you automatically convert it to Bitcoin?
-Yes, the balance of the bot is calculated in Bitcoin (BTC). When you replenish the balance in Ethereum (ETH), we will automatically convert it to BTC.


-How can I withdraw funds?
1. Click the "Withdraw" button in the bot
2. Select Bitcoin (BTC), Ethereum (ETH) or Yandex Money (Yandex Money)
3. Enter your wallet address
4. Enter the amount to withdraw.


-Do you have a referral system?
- Yes, we have a referral system. You can find your referral link by clicking the "Advanced" button, then "Referrals".

For each person who clicks your link and makes a deposit, we pay 0.0005 BTC (~ $ 1)


Thank you for participating in our bets every day!'''

btc_text = '''Для пополнения BTC с внешнего кошелька используйте одноразовый адрес ниже.
(сумма не менее 0,001 BTC).

После чего средства поступят на ваш кошелёк после 1-го подтверждения сети'''

eth_text = '''Для пополнения ETH с внешнего кошелька используйте одноразовый адрес ниже.
(сумма не менее 0,001 ETH).

После чего средства поступят на ваш кошелёк после 1-го подтверждения сети'''

eth_text_e = '''
To replenish ETH from an external wallet, use the one-time address below.
(amount not less than 0,001 ETH).

After that, the funds will go to your wallet after the 1st network confirmation'''

btc_list  = ['39G2uCXzpLHBtrxxvtsczWkG7yFm5NMy8g', '14p8j9J8Lg7AdxvUur35Mk5q268RQYKjcY', '33e5EpZF4SYW1MJUnpucz5yoFmfZX98sKk', '34sSUvbYfBHk9n4gKcqjs9omepysuCqpQR', '1BBh4d8A4C426WD6bfCqmmJwVSCqmvWJpz']

eth_list = ['0x990b30e1c727a5DcC980F5677BC55b3Bc2834366', '0x922319a6637bf8e1d449b662f2c1b712b1485112', '0xe96143edf3e57c973d2ce4816671db7b1fb4a635', '0xbf91ab9bbdad9860660499feddd6a1166940ea36', '0x5a8644696010c21a19b146a4db090576514fdb01', '0x3e664146be97eaf42c1c888222d3a1982d9017e8', '0x0f2eeacb00d6568250e483d69a73c72f5aa36bcf', '0x0b2c941e15b8636b8ac79c5c79b7438a66421c22']
