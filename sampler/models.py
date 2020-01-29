import os

from django.db import models

from sampler import audio

class Sample(models.Model):
    audio = models.FileField(upload_to='samples')
    
    def download(self, watch_url):
        filepath = audio.download_audio(watch_url)
        filename = os.path.basename(filepath)
        with open(filepath, 'rb') as f:
            self.audio.save(filename, f)
        os.remove(filepath)
        
    def slice_(self, start_sec, end_sec):
        _slice = audio.slice_audio(
            self.audio.name,
            self.audio.path,
            start_sec, 
            end_sec
        )
        slice_obj = Sample()
        with open(_slice.path, 'rb') as f:
            slice_obj.audio.save(_slice.name, f)
        os.remove(_slice.path)  
        return slice_obj
    
    def as_samples(self):
        samples = audio.get_samples(self.audio.path)
        return samples
