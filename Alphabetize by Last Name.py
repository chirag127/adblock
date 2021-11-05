
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0

# write function to sort by last name a list of sentences

def sortbylastname(sentences):
    sentences.sort(key=lambda x: x.split()[-1])
    return sentences


if __name__ == '__main__':
    # test the function

    # create a list of sentences
    sentences = [
        allconnect.com  # div.row:last-child > div.col-12.col-lg-8.offset-lg-2 > div.entry-content > article.bg-blue-bg-pale.rounded-4.p-16.md\:px-24.lg\:px-56.mt-24.mb-24.md\:mb-32.text-center:first-child
        androidauthority.com  # .bHbgTQ
        androidcentral.com  # .article-header__disclosure
        bloggingtips.com  # .disclaimer
        cnet.com  # .c-head_disclosure
        comparitech.com  # .ct-ftc-disclaimer
        countryliving.com  # .affiliate-disclaimer
        countryliving.com  # .bar-content-disclaimer
        coupons.cnn.com  # .disclaimer
        creativebloq.com  # affiliate-disclaimer
        creditcards.com  # .c-advertiser-disclosure-toggle
        creditcards.com  # .t-disclosure
        designerappliances.com  # div.affiliate-disclaimer
        experian.com  # .adv-disc
        forbes.com  # advertiser-disclosure
        goodhousekeeping.com  # .affiliate-disclaimer
        goodhousekeeping.com  # .bar-content-disclaimer
        laptopmag.com  # affiliate-disclaimer
        livescience.com  # affiliateDisclaimer
        manofmany.com  # .disclaimer
        mybundle.tv  # .disclamer-text
        pcgamer.com  # affiliate-disclaimer
        pcmag.com  # app > .text-xs.leading-tight
        socialpronow.com  # .infobox
        soundguys.com  # .post-disclaimer
        space.com  # affiliateDisclaimer
        techjunkie.com  # .article-bottom-disclaimer
        techradar.com  # .affiliate-disclaimer-bar-slice
        techradar.com  # .affiliateDisclaimerBar
        thepioneerwoman.com  # .affiliate-disclaimer
        thepioneerwoman.com  # .bar-content-disclaimer
        thinkmobiles.com  # .disclosure
        timesofindia.indiatimes.com  # .disclaimer
        tomsguide.com  # affiliate-disclaimer
        tomshardware.com  # affiliate-disclaimer
        zdnet.com  # .ad-disclosure
        zdnet.com  # .commerce-disclaimer


    ]

    # print the list of sentences
alphabetized_sentences = sortbylastname(sentences)
print(alphabetized_sentences)
