from PIL import Image
import os

def convert_to_webp(source):
    """画像をWebP形式に変換"""
    try:
        # 出力ファイル名の作成
        destination = source.rsplit('.', 1)[0] + '.webp'
        
        # 画像を開いて変換
        image = Image.open(source)
        
        # RGBAモードの場合はRGBに変換
        if image.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', image.size, (255, 255, 255))
            background.paste(image, mask=image.split()[-1])
            image = background
        
        # WebPとして保存
        image.save(destination, format='webp', quality=85)
        
        # サイズ比較
        original_size = os.path.getsize(source) / 1024
        webp_size = os.path.getsize(destination) / 1024
        
        print(f"変換成功: {source}")
        print(f"  元のサイズ: {original_size:.1f}KB")
        print(f"  WebPサイズ: {webp_size:.1f}KB")
        print(f"  削減率: {((original_size - webp_size) / original_size * 100):.1f}%")
        
    except Exception as e:
        print(f"エラー（{source}）: {str(e)}")

def process_images():
    """指定ディレクトリ内の全画像を処理"""
    # プロジェクトルートからの相対パス
    image_dir = 'static/images'
    
    if not os.path.exists(image_dir):
        print(f"ディレクトリが見つかりません: {image_dir}")
        return
    
    print(f"画像ディレクトリ: {image_dir}")
    print("変換を開始します...")
    
    for filename in os.listdir(image_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            source = os.path.join(image_dir, filename)
            convert_to_webp(source)

if __name__ == "__main__":
    process_images()