import tweepy
import json

class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

def output_json(data, output_file, output_dir='', type_='w'):
    """データをTSVファイルに出力"""

    if output_dir:
        output_file = output_dir + '/' + output_file

    with open(output_file, type_,encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False, cls=SetEncoder))
        # f.write(json.dumps(data, indent=4, ensure_ascii=False))

def gettwitterdata(keyword,ddir):

    #Twitter APIを使用するためのConsumerキー、アクセストークン設定
    Consumer_key = ''
    Consumer_secret = ''
    Access_token = ''
    Access_secret = ''

    #認証
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)

    api = tweepy.API(auth, wait_on_rate_limit = True)

    #検索キーワード設定
    q = keyword

    #カーソルを使用してデータ取得
    for tweet in tweepy.Cursor(api.search, q=q, count=100,tweet_mode='extended').items():
        #つぶやきテキスト(FULL)を取得
        tweets_data.append(tweet.full_text + '\n')

    #ファイル出力
    output_json({'tweets': tweets_data}, 'yahoozozoツイート.json', ddir)


if __name__ == '__main__':
    #つぶやきを格納するリスト
    tweets_data =[]
    keyword = f'Yahoo zozo since:2019-09-12 until:2019-09-13 -filter:links lang:ja -RT OR @99999'
    
    #出力ファイル名を入力(相対パス or 絶対パス)
    ddir = '/Twitter'
    
    gettwitterdata(keyword,ddir)
