from radiant.server import RadiantServer
import settings


# ----------------------------------------------------------------------
def main():
    """"""
    RadiantServer(**{k.lower(): getattr(settings, k) for k in dir(settings)})


if __name__ == '__main__':
    main()

