import threading 

import listener
import downloader

downloader.first_run()
listen = threading.Thread(target=listener.listen(), daemon=True, name='listen')
update = threading.Thread(target=downloader.update(), daemon=True, name='update')

update.start()
listen.start()
