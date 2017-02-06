import inotify.adapters


def _main():
    i = inotify.adapters.Inotify()

    i.add_watch(b'.')
    print("watching started")

    try:
        for event in i.event_gen():
            if event is not None:
                (header, type_names, watch_path, filename) = event
                if 'IN_CLOSE_WRITE' in type_names:
                    print('file closed: {}'.format(filename.decode('utf-8')))
                    # run further code for closed file here
    finally:
        i.remove_watch(b'.')
        print("watching ended")


if __name__ == '__main__':
    _main()
