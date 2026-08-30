from client import ZeroShotCrossLingualVoiceCloneTranslatorClient

def main():
    client = ZeroShotCrossLingualVoiceCloneTranslatorClient()
    res = client.translate_video_with_cloned_voice('https://assets.genpark.ai/video/science_lecture.mp4', 'ja_JP')
    print('Cross-Lingual Voice Clone: ' + res['voice_translation_id'] + ' (' + res['source_lang'] + ' -> ' + res['target_lang'] + ')')
    print('Timbre Similarity: ' + str(res['speaker_timbre_similarity_pct']) + '% | Lip-Sync Accuracy: ' + str(res['phoneme_viseme_lip_sync_accuracy_pct']) + '%')
    print('Dubbed Video: ' + res['dubbed_video_stream_url'])

if __name__ == '__main__':
    main()
