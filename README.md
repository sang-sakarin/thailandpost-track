# Thailand Post Track


A Python library for [Thailand Post Track](https://track.thailandpost.co.th/developerGuide) API


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Initial a Object](#initialobj)
  - [Viewing Track](#viewingtrack)
  - [Viewing Token Expire](#viewingtokenexpire)
  - [Fetch New Token](#fetchnewtoken)
- [References](#references)
  - [Status Code](#statuscode)
  - [Language](#language)


## Installation <a name="installation"></a>

    pip install thailandpost-track

## Usage <a name="usage"></a>

    from thailandpost_track import ThailandpostTrack

### Initial  Thailand Post Track Object <a name="initialobj"></a>

#### Parameter:
  * ```token_key``` <b>string</b> token to access API [Get here](https://track.thailandpost.co.th/dashboard#)

#### Function:

    TOKEN_KEY = 'X5RcT/DOF@ESK_RxMICNP8PTW=Dm...'

    thp = ThailandpostTrack(token_key=TOKEN_KEY)

### Viewing Track <a name="viewingtrack"></a>

Check status of tracking

#### Parameter:

  * ```barcode``` <b>string list</b> tracking number of Thailand Post
  * ```status``` <b>string</b> filter by status ```default``` <b>StatusCode.ALL</b> [more](#statuscode)
  * ```language``` <b>string</b> language of response ```default``` <b>Language.EN</b> [more](#language)

#### Function:

    from thailandpost_track import Language
    from thailandpost_track import StatusCode


    barcode = ['EF582568151TH']
    thp.track(barcode=barcode, status=StatusCode.FINAL_DELIVERY, language=Language.EN)

#### Response:

    {
      'response': {
        'items': {
          'EF582568151TH': [
            {
              'barcode': 'EF582568151TH',
              'status': '501',
              'status_description': 'Final delivery',
              'status_date': '26/10/2019 10:00:44+07:00',
              'location': 'RONG KWANG',
              'postcode': '54140',
              'delivery_status': 'S',
              'delivery_description': 'Successful',
              'delivery_datetime': '26/10/2019 10:00:44+07:00',
              'receiver_name': 'ยุพิน/ภรรยา',
              'signature': 'https://trackimage.thailandpost.co.th/f/signature/QDY4MTUxYjVzMGx1VDMz/QGI1c0VGMGx1VDMx/QGI1czBsVEh1VDM0/QGI1czBsdTU4MjVUMzI='
            }
          ]
        },
        'track_count': {
          'track_date': '24/03/2020',
          'count_number': 6,
          'track_count_limit': 1000
        }
      },
      'message': 'successful',
      'status': True
    }


### Viewing Token Expire <a name="viewingtokenexpire"></a>

Check token expire

#### Function:

    thp.expire()

#### Response:

    2020-04-24 17:30:48+07:00


### Fetch New Token <a name="fetchnewtoken"></a>

Fetch new token, if your token will expire

#### Function:

    thp.fetch_token()


## References <a name="references"></a>

### Status Code <a name="statuscode"></a>

Status of items. Click [link](https://track.thailandpost.co.th/developerGuide) to show more detail.

#### List:

| Variables                         | Code         | Description                                                 |
| --------------------------------- | ------------ |-------------------------------------------------------------|
| ALL                               | all          | All                                                         |
| PRELOAD                           | 101          | Preload                                                     |
| ACCEPTED_BY_AGENT                 | 102          | Accepted by Agent                                           |
| COLLECTION                        | 103          | Posting/Collection                                          |
| IN_TRANSIT                        | 201          | In transit                                                  |
| PERFORM_CUSTOMS_CLEARANCE         | 202          | Perform customs clearance                                   |
| RETURN_TO_SENDER                  | 203          | Return to Sender                                            |
| ARRIVAL_AT_OUTWARD_OFFICE         | 204          | Arrival at outward office of exchange                       |
| ARRIVAL_AT_INWARD_OFFICE          | 205          | Arrival at inward office of exchange                        |
| ARRIVAL_AT_POST_OFFICE            | 206          | Arrival at post office                                      |
| PREPARE_TRANSIT                   | 207          | Prepare transit                                             |
| ITEM_OUT_FOR_PHYSICAL_DELIVERY    | 301          | Item out for physical delivery                              |
| ITEM_ARRIVAL_AT_COLLECTION_POINT  | 302          | Item arrival at collection point for pick-up (by recipient) |
| UNSUCCESSFUL                      | 401          | Unsuccessful (physical) delivery                            |
| FINAL_DELIVERY                    | 501          | Final delivery                                              |

#### How to use:

    from thailandpost_track import StatusCode

    StatusCode.ALL

### Language <a name="language"></a>

Language of response.

#### List:

| Variables         | Description            |
| ----------------- |------------------------|
| TH                | Thai Language          |
| EN                | Englisg Language       |
| CN                | Chinese Language       |

#### How to use:

    from thailandpost_track import Language

    Language.EN
