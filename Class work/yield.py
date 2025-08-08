def stream_video(chunks):
   for chunk in chunks:
      yield chunk # Yields video chunks on demand
video_chunks = ["Chunk1", "Chunk2", "Chunk3"]
player = stream_video(video_chunks)
print(next(player))