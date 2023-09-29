import requests
from fake_useragent import UserAgent
import os

def check_or_make_cookies_file(cookies=None):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f"{current_dir}/cookies.txt", "r+") as file:
        if cookies:
            print("Writing cookie to file")
            file.write(cookies)
            return cookies
        cookie = file.readline()
        if cookie:
            print("Cookie found in file.")
            return cookie
        print("Getting new cookie.")
        return None



def get_cookies():
    ua = UserAgent()
    url = "https://chat.aivvm.com/cdn-cgi/challenge-platform/h/b/jsd/r/809128c5a88f8335"
    
    payload = {
    "wp": "gtyVHm2QH8yHI5B2q24$fVmv$ad$bYbDDmQ2NL$lXvEX7y$6lUSBX82K$Iqycott$aTD$p$DvDy2$+D2wBkVT8t3sPVlXxtdazK45c-VwxHJdF$26lBib$$9$SDmY$2b6$J$y73g37$He$1Nl$HNo+$5npHaQ+$Txql$2nC$2ar5dK+4Q$AD27-yQ$pGo8Pjel$HQUOVxc2$m+IV2LaVeWrfjtmKzl$pDX$alyi2oq0EBK+qr$PSri$25hGukF9Da$GSQiqqKCLgzQ9Sfi0PY2eUfh$InFigj$7KbDQ998F4vVdHVESODUcw1cJozTQ3D$D3ocfB56zQaNGdozTBku6H6nnwtusAOeS$p7El$$AR+rRBb2Uy57YHmjw1HVlp4wRj7$2IKwX2sBVxFiz6uwTT64IQUGwzgzznJ7kenTV$vrOwQvbSRFLllVmohfUqNx8wwwgJ1bw$EoXpAYx$$HIzOu-c9dDb$pvLPjISOlmV$nEnmmabltt1yvaDK28QfU4TQ8EoqOY+pw9er-K1NvJA915e$c5u4et6IYIQol+f6GfS1K4oSLywmD2pfGycTJ1vgIDyyzRWLiV6im$jlC5uzq4fnRXigfk0anR1Y4Ytuopo+Lbn0p8qy5iv+i8XujQbJlmM8Gk+9hcOBl8mqlF+jr+yWnJj0F5jOPB-kcAOyHCrYEyH7EE2po$xaVH2Bmj-$1eMJuNsqyl6pDG2I28$fkiM2$SHjKeQ5UBRzHj$AkmBg2j$xs4WlVg$23j8$U$lLONLXmbt2V+$XIXIIVlVedGmVFlU7x3m6AjW5y$$x3Mg2l+llKlmy7Ho$7edjf72R9mihuBAb8mWplhm9-Vz5U$Ay$YBDedk5izaXuVIT2ox32wxAm$BSxgTQ-vsYgHDmH2r2vHQC$8J6TDGOoplY6$ait$VKumyXgRQc$BSTf6b$YyXDxW$7c2elXR2N2D+mRHD8HlcielSmq-A81qv$AQDDO03q3HQrqzlX2ds6y2DUvVTdhHo2xqbX+AlV61xQ$TIX1Va2VLCdyVQwzxVs2k5xedx$V1wQHjL$$gIvngjI68ytO0dV$mrtDyHn0alPXhYQaVVIyaJOXsbnYdzVVSOAlXy44Sg16erxlJjfIu58D$Sz6xjXytsvIfV8Gel53$+fx$OG5i-d1yV4NSD7RwyHD$YvTDi$ya7cRHPSIJj7v3fppoIfdcy7HupjoqtB4rAUyXiHlcVelXc4RLmytOIzb$PLAaMFOlmgLpYY4zR0Akm2QYuIKwxSfwImDzX2rSPdQLg5mfDDrmwEi7$+Bk+$Gr7iob$fyKAI7C50ByQHdmV228PtqgkgGqqwFMNpc1VMo2L5FKgBnrs07cIKxUtmJo82yv70gsd0fuLlYWtHBESANHFXJ+Hma7LH3dDi3apSy45C$D+2ryElb$E0nklGeT47SNOdWKh5TQCAo6rUmm6yX0X6r-GOlmkY6$gyylXzPNvceT40I2ch8-2mcWKulkkhjKh+ErHmplizkUG$YRayIwnmfBCzjWeTAgzDXFPKnGo8HDe3EIDjI5$T2nsKLbIJO-2a1zhnmb2Br+TkaGLVh$iHMqyc$SDK5W2qqy2tmDyvFRW2r3aIbSmxxtHTuXPeNmqRID+RBGYWxJRNje7vgeUNxHK48fDuD16qTXvMoyKqPo$FyclQJ7$GkJVgDmpyJDNntTfcrHyBMQ$XHxGRooO3SxaTRpPuhxDYT32U56bVgdH6xDY$DfiIBBx69dw12Xfek655tayHxavVv17na1fVEvkmxVH$mPjsjwXWTM4UQoaR0SlHYYBaeUBaSxTRf0cX1xBoqT3yeyS81tRAH+7e3l4e6OVK0y9DbOx-nq4kRbTj2DFUfaHb6Bfrx3Db8W2MTDxe4$mHlLM$BLqgl5hFNOdDI1qHJT2$m5gcbYHJymGYCtB04nJT+KILBgRy6LxkLHa$eqYmbH1YqGcl1k2rm-fbIzg3AVsAz5Ozc-ioihKAl+DbIyOj+2zRy$VtwHTR2xcMnvIDjd$tMCtyQ6$$6v71l8lj8xXrt2VfeoyajUflC2KVDe$w1f3rNqCwmd5HG61EX78CD5WeH5PH2b77$soUlBohoYiew2+H0qxKmRMKQUMU9uijl0Vubyr$AD7SmP6v1lzqRBH1X67CYuU3$X8or2y2J0wMG$Bo2yS$A6r6G+9viV3wGeA2iuvhYii18XaHTk81slHj1A32TCR2e3MDJXYWwwoHr7ryWfnGlHTKUnGx2OKKN1Sa-YuuXelOXwmvx52Y5Vey7bNgb2K-7STCyT+rmsImCK9qQ21JmX-EmHACJil05V3u+SmVY8nrNuus1sepJaXSrubqTN7fIXgHzswo5W85Hk$w-YtnCvhG2eKDX2NP8yVr2$6pdnm2KGTeldpRzYMh8+KwsbqgIVhAVsAQ+E2Ox46cztmVlzIf4rVDHO9qkqNkmvs$CV$$C6aJDJRjSr$HBfLrUSC5gm9cj8dDrlH4v4bpjM92PqOo7uakVilX$Le5QOG5I-jiR1vebUrh2W6F9Y-nIDT8VqXxDc8o55D0HdHMadegEiEFjnTbU61Kn2a+qDHwzTb4pBSx5RDQHb2+BQ8YR$Kbs-+1U-riEy8Caf1o-E+TCJANVRau2bVcV82tiv2ym7O5uNwXXGXk8V4wzTqvazIpVkGKWr49H8AWYFJLDGuyFAsOFGrXmbQWi3JrwPgqAya3wJsw31lumMpXfD1Q5OsVjbKz+alp+jIqmoOeJ3gi8DLvVbVwhXSbY4JJ5K9j1Y+6+W$bFSmXTcB3G4qRCb3NP6vxOfo8YsgINPFzfNVb2VfRrbK5m$03qpv+bUMn8jG3KI2VGfo-Qae$Rdy1-thPt9jE8zRD72+$Xitcyc7Ir2fhILGeB0TwdlImjiAtDcux8seD$$rN0ih-G52lHDnawzi$FXCzs+HykvqWk+CTA-88e+gDaR+N2kL$AHHy+vi+BLac6HL8RHlROQyzE+G69xGJS5o-oP2VeNxqgQuoFeHmKVG0YSUiKGeTnuGV-PX17dIihqw5m6vEBorXqx8zt+KSDxDH84FJjcoLM7o5MxDRURiKDc+O$4qOD7Ut1wfJRGIQGj0KYqqTrxSqXDfKKfh8hU$-MNJUzovi5rgi53NdHQ7g07D-$AxVpt7XgXDtYNPi1H$VOkCsTKqSGz-IEMsjuuCHlmkX+pu+AuIiOz0+SDWiC3GbLJTMyW7WtrKREmHKwCBa$uWeh40Hrh7clUBscRUL7kXVQsBP+BY2OtUiLH+wUNF4UoCVqwMWMUn0bs5Y1s+etbJhzE88B+ThkuKdETr8dMFKqYokCsaCooFxl5VYWzSmzhviTLOOvGhUJxuaGY0Tk0SGIPFGAGzi9oRx9wMbPkGj5E4cqNCs-1znPN8WYh0v9ymfuW6MRMJW3Mi7Rho8TMdKi-LJd9Jswo9oRaT5cP3as1JhdEdKdJgx5h6wRwdK3L3$nJiwoi7D5h61TATc61oQegrD+1i1uEdgdKK1TN2qJh6jxDaqKjuVOcK1VNdKdp3D-EdpJ5JhdpsWKpTcTpw3Ryb363KjOyQ$Iyb3J3KyO3oishwn$PTcR+dK3YifuE3Rz+uW5hK+V43KTc3$R03Inz20s$nyo4sL6ms0RfrqcjgSm2sUfVKHTcT2umuET2KeDhsR6kJhodzi6KdMTmoVndudRlCiyxJhoxwFuXV6Oj7x9O2KTxKhLxK$Gh6vKUmvsCsK3JVioV87zJ37uJsFyjVhwSSGujIS1KmfpNdGRV-61exKwiRWuEJiTiT53A6AejQXuXAFsXGk5eO5VyDhw5VFshT5RF66ATseO5oe+BbBGNTeO5R5uBAFuy8on8oyxoI-K5dK6lQkLSCtQJdxlKoSbN94uETQASS7JtPQ+S87pQDhoXAh5GV6SNRX+UAruUbSOUC7RX-Ls3Tcu-s-sPVD1y7h6QT5ssBrTEKtyEJKeUoRAmokrkpkgS7uBRn-oafTTYuEwh6O36xmSPRB2OJOot-O6B-X3lPIAWsuiM$msBLawFBocALXyS3S5YOMrj9lRhoQ92Kig67OJIoolDcFprD4$lIqpS75Bicnpa5reB7bA2mvaVHi3j7$$$LxM62ie2x7pjG$2Hz2XbWrnyl$ldJxEOkdoDW4W90dKFIiYmiFojQ4mj5c0m6IYmMrx4l2RMeFs83vV4rOp$4r-xg2er9mgvhbcD3xl9dKFjmOw$l2ureKGFJh7w050mGFztF6dJFwIw8jtJIK2T26BvFJox0dlHLxky1R52LHrD6$q2+bjrtHSeX2RbXbniVJj$+msa+YYTwOdtV$HwFms80RMtbOQMzOLvtKMjA7SOWhlmevO4rbuK$9qmXrueOMzxReYvYeJrgxSO2RkrF22$b2VVRv2mGuqreIUeJroMIl79t$bH9JvjItkDTb7yXmP6Wjle58t2lw5O5xbxuiVRQDpAdHkfWyR2H5NmHD94HIqHeedeX$$mpgXgXTVNDs$p6h$y9jIW0mVkVYF9by$jIUQ8$kVX8mmjIp5g0DFx1eF46g$O5gXglSFR$OUW$QF75NdKMX5K5jJm$Q5iVM686JReJSJJR6JJyRVaFv$18plBQ+F3vhlJ8glFS5ALSeY9Yg$saOU4SVFjF5lh5tFsa+B45glu55xb$GJBoV5TYVUp6KDi8WYAmp6l6wd454DR7Y6oe6916gJm$nJ8$oeKDbbODtY7o3$tG7B0oDGQ$XGR$WXUGMj-VFVg$PmEDJ5MAtY$ruD-lIVOF55hm3$d78MJGyjxGqQIMSVI6WqgVhYWeCddDnamrmmn6mVoeN8M5w6-XzRIy+XW0CoyXEigo3$WX$DzQrwLJBo6Anl-lBo+BNRjDJ8k5qqg$vmddPlelpNJ355Y6vNmmLjp9FNg$+BkRk6gDNNoN$Bp6jDTNnVuIf6H5g$qG3D-NcVDI+mKinNENQDwIWNF6Kl9BIg$gKlMjQDrDJetgfrrByjmgbgogQDNtMgg$9B1gBgg$$NnQ8$+glg2gVNJefyqg3$QgyjwIeY56-I5$Ggy$zFr$gg8$5g4gug9BKg0g3$LJeV$AmB4Ug$EgzRLUgVGB3UloJBHR0Xlzg$rNjDKlXGVScMe6aN1Q4Doz3UzNuDsXXoLN0z3XFDLNDjQQ9YzRyIdzeyL6t3izeyFzUSt8gVqX2wBoFX-z4UBoJD1F3$-l9zVwKSh$dDeV4A3$SVwry5y$GFrocVtDxS$yRG0+qG3GYnTx8$-VzV$jaQ7$nAOqXnsat5EUN056ozI69UyoTVape64GmV9JIMGB5nyoFBqDRBAScjg$$VqDFVzVrNgDVXJ3$V4VbB+BtSqRCnykw$kV1N78XnjkbBiNPoC6mm$VTVFVLUjov2KM9kMkk$qijVzJE58$Mjsoyp3$8kFV0kpwxkg0nGBQheKFCn+k2kzkgl4kFVh7fm6z$avASNHR$DVUwRRX8$Do+1JBskNAWk56DH1RMig1JRTn6HaGinmGy$oUv$UUmmF$YmJq3$i$YwkkFnqD2UJdOn3yFVB3YUs6Mg4GuGFn5HMjq1RRDGCdFHsnO1RRoexV09wXy9hHMoP6$vMHNB5HWXWeHHakmo7$6AsXQ+$6yGTSsj6TUoPmTneTakHgbX6T+BiYXN8maopTEa7$I6hBjg0HaTNX7$KlhHrNNMAn5TI65H4JiTCi6T2TP6xHTT5HDgMTOTFVHoBbyNaS6Tkj3TD+9$cT6zxQ9TnSs7BoXStSSSBSQSy03$XSYUlSQ$MUwUnQce3y9M-84DtbV8CTy$biq84dYowp6Sjy$jriy$CBkoTo4oCd9nLUS+XDhe56169nSkW6Co9nENsNJ5g$zVFStYGScN4R-doeXbclI4l4JSIQB4uR3$t45SsFE$9RD4M4b414r3gVa464k$zVMkR4xVi$Y61HR4y7KoAOt4QwRRXHVHGVQHoARHmmT4XR449Hz4b7e4M4lDSDHGI4jfa$H4tfI4+FJNlV16VTKpPHefM4aoT4j9kOm$YfnV9fCp0XafI4pfPH2fP6nDcnK$UfaoH4Jfkz7$f4vfn5gfC4aoVU7zzfP4rfP6ffXoOfP6I4c3Uz4$VSPfv56AWj$aBAQ2H4Wfc4BrC4WfwBcniTKo3FqB2xtTK$RBCQIMqDB63aAOPFaG+M8$1f2ubbxug$iurNnS+Slo+BPmSVb$TB5u+SR$Gu-AODBzoNcqlV0uEuBoyXxoL$ykn$v$UO4uFlK$ofWulDyrm$sTv$7uB-gDU-5umo1l-V+XgVD52nVpOiVI4d94ODXSIak4Vfy$Y39RWnsUTDI-oNTYcbrSp6Cdi+Y$5u1XJo6in-5oRXqu6S3y$An+qDP-OOVhjhq1BQcN16Dh3yE4h$fH1Q5uP-ohRRRhBhyoR$ehBhaoBDc1d2NRDi9hmfSklf2hoNbhJfihF-FhP62TViTltzbhqDIVz+JhXhQNmNwhqDMl5GuhP-iuKhcn9$7uPhN6KhRVKhq4wrKhP-wh+B4XocjxAh3yLjWQQ$3yF6xSWDwhoTkn0ozB-I4XLjqS9h4R0SaAqcP$OD1wfhkh1-P-BDQDjc4Bnw7csj$4qcRksh3yCGUN7$OcLcLG9hifK2p6whhnjoLYbcRBv5IKhe1HIKvhwhMAx$heMcPmT-bKFcCcJV9$w$OcpKM$LrXhonLuCc8KjVulFfwh8KwcnhK7bc2OnlRV4DNKwhRTtlb$nHOq-KKDW6-KkVzVVIiTR$4SWK3FahCcdeOhqwMAllWKOhsXRXheoCu$NoWKHckG4$u$WK3VmVn56COVTD5K$or$ODWKnDv$lVUOFC7$iKzc9hde7Kf62C3yadDXKQIyS0WKhG6-ECFXK$3yPCWeIyDEK$cVECilOIWKUjs$jV9TrmXE1QKQvu1C0CkCbcde3Y2a3mtpWDloREQVnorC0x0hMEGh3ydePewx0otKcjWKOz4bVwkEarJzRfL47$4Eilv$zEuN2CKCEawhLDYSNq4CAEXhwhVUC$lLGVh$whHEfzYh7$LCk4CceYNQRK9LERbSeLkKFEHJe6wh0LY4KHwSOcxLsFVcBN+LjFLSQcnc3yFL5$pcSUm$0cOqxcWj9hTL$KPcmhbcELEGs-HLgL5$2K+KPLNLKaLSIsxKP-TLaFlVmmXhTLI3naOvXnYsysINP$HR6NQsysDFvp6s1SlJ7LTSdLgLSorLIL0sSs5sxsYsn+Ik4zwdIkgdnnfLbogdgNtJcsHnDAg1Kl-sKMPsj2-kgVnuY8SH9HoHyH6PIM6PPkBP-4yHBuqT3$RPXP5F$D5tSVIytPLsK21P$H3P0Pa3mPa3bPqPdPSPR$X5elf48PmPTpaPMKL$UO1f1nNj3fAOCPNOh$+Bz5gNqnLUjm$66L6cCdPP4XjVohDWaPqn-VpwohgDOomPRWpwLU+TjW$jbWdksXO$IPqn3nv$0n$pb$3DHNA-CP7WAWKoJWKNqqsPvWxViW$6kASWqnHWQW8Oy$CPHWiJy9pFVCtwVar4WS$-zx$5RF115$8rpS2tHpSn0X$M1l4DOuW2l2y$0IaTcI$WUiBCP$1RS4emRFu0qn$Vn9Ry$9AU2A41SalmymlmP17$46gDrEMrjn0$jgoKV2rD+vJ98Xg8KT58eSDYwnTlzlygt$J7X0y$rzo$JD2ixnr6DfjTlHwFgoCyA-HfKFNSabyd6PgbDAerkVPxobb$PDQa2jIe75837$jSI7S5GG72AYmC7jm3-RlBtkSOrcbdG8btK2RRpJ7s1jx3mmRcVJjQNHci7o7rzmnjbDlUcgDxMQDCjGOEU5rgweePHhecYvAvmwegDxyDVJb5XiDMK6AG9lfUcdm$dgDcyQjaexAHwenDHEByErlN2lIwHx1eSLRlN2kt9$1jLYvRlgHK2OD9jbB$Mat$8dbAB97v$a50y0dgVue16p1iyvhVzjPeAE$2bNz721V1nRXOrAI7kBaaQY2w1M2PSyMC$Oe7txu-bj8$3CxFrA1nVHkTa0TGXTB7pc364dKQmtCQ76$F7tMRnr7oUg+5em+$Ozx$r1qolnU7+UOCy5SGaVX2twMGcWfVl1a525$Kep+aJlUanS+yiDolnm7xacSryrjFl-6yeTCyvtACDL3myvaRxy+0x8dmSBvlmxMwDIfHecEelkm-$JyR6bbrpiJzDMPQ+7iMv$HGXwq5lpHeXcLRUT8M8pOEVT2CxJgUreQHMo4bJlbSL9mBH-$V2R2bA6rEB2VnIfG582m25$vSPE2+AezkeSVvb$VwfeaTQ12O$5msONc5x4xPHbSON5zaegHxge63zKjncMTSa-jWtmDXHH5HTd3$BXGMp056Rm$e6xISapuM2TcxEUIyPDlhTOJCxseqg9My5lc7OxBI9ve5b4V+TRe1Iie5Rqf95RIv-NI3z$p8mIe+e3IXDctwklU26vWes6zaLhdLjCtm+H0BfSjHuXMUuH8p3IHjDVxFIK$z$$9q5dro0v$tTclppo$X20vJCaWf+4Dme6edzRc76FHMHq$pIRal$H64Fj5Gu2rJLk7h$Y5Rtddpg8Nl+yeVAH4vJrBiwJlibHvitRyipTcbADIFcvjUGo8TK-lTjIMNF2$$fxvuWT1v5w5aL0gs7e2hYtOBF7lNn7$bz$ll0UTT1KrHj0lxqapu6HQmDRb$RjEycNmeAWj6$Hy3UCN5K-x7eM+losi5xvikxyMY$L9$CvxRXb19OqIMHfle6FBeqglolaJcrmbQIMPSpAok$1ABbjD$zLY3vfMVXROxF$O$2Sj88SOi7J3Pl8gltRB$NaLRaVLapw4lbYqi4n+K$gCxNFk7FV7dszl-moJT7A4SYDNboKuNHxn6E333vvh1mO7ru5Y-ITQ68vW9HRxY-caAxcGfq-6s0TwveMtkViNAHgiMHUK56IiNAyIrfRmK1bqdUSutyJfptxb0rRFDDSJLCuWzQiakAkeFy-l+b-$76hymdwrK7ARi6WxYnnaXYJbz7N6tD-WlQwYBqiFVYoVG7ciT6qiEO+vdAXQJb$BQztV9AcC9j7OVrVplY+g7Y6AOu7tXkHdlal2Hb17UcB8-AyrJbv3V1XvD2kNqwRnniCqxY11rqK3dwrTSE$mALqt5OJp0XxYAI2yDhOFiMkPoDRKbKdOu7FVCMVGLslIFc7OC$aQFSQKhX56yBTCaJjrK9OKiKXs+iR$rKpS78T6taDTBYTy4BeBunV7ggmJgONMyGp49FpoKxSsV5$7aDGLomUQIAdBhoDGrWi9kL7N6EA2SlQwh7Vjj6J4uOg-Ril1ARVSD7FxAK67gifX403DdAJm4IAFV-a+PNvwb4cdc3xY14aNymD5AOIBuVGf2$+Ffiy$lYPKXQJNRkA5FL1xnl82M40$SoujeFYeb+jnq9jEI-f5Cx1YrygoRqDhfyR+jdVVeoB82mXR1YEAXnGuKXHl$S2tvSnB-JR1zaUvKyDQoiVcLnjS25AzlfqfcrHJRj0Ab$xIIeX$8RYYqwQjm-VcvJxGgebbxDLsHtxJBmFD6w1m51eTJYI9UP22pJSvIbkaF2g2v7ulfIX$AM$4LqR$csizHFvgV+0RGBhwSSdVFXrRwSEp9OYdbrJDr5iHu44$$I56calhxfxcmwvy$a-3yHrAXYEyIQaVfsrfvTxQ+dUqvyLHLbfm31QQp+V7Hi-UNYlRLnQ92$m2Io28TU6lPS$L6L4paIMGIytHmH4j6$uU9Dytmwu1v3xPUo2S2jJFWYM+6P2N6MEFeVrM+jmvjcOjL6Vfueg872btHo4jfc1KlL01eyjS32d9mmL0OkEj1yfgFymKhRD9srwyEyNmL0OLx92xN$Qfm3qPSEIV229wvQwjgj9vdJg25nlLv7uGX9QD2V5IT9fVHc6T$uatD8q5gGMbJQYI$68hTdyHlV$WDc9cpBlB1au4PtjXnJzei+Mhzd5nlCceACyiJoX+gQL7s3goDJB3QW6Lpnesy5P$KqNpPY$IeUGj$r3Rs$vCfB35MguISO1t-y3mCkBb$CoQtxhdoMgoYIjb6m8klTl$BCxoRqBl9bE9xbu$7YaeL77JRzXwaPGc9ySu7RvVwayoQiA6er2gALmxbqBB3XYVNfz5OboEVlcdh1H1Mpum5$J$ctkorJoI5NVV58SkrxJYbbj3Bobx322JzbXNRYNjDj5IJoI-yLLlk$SV+JMY6jaXzTHurdJKYGo6Bzw1y$o1unlFIX3Y$AzJ2DYzNosm8$Cf-JTEOqaBzT2pmmB2nQD9Exceb2cJzbKTwQ6tmsfoV$rt1agqXazXpxqXBDHSH01hfRMQrN3TkYMGpfIjhnH$BmsxSMoXabriamzSzT-TQGw$1lInS3CeuUrrYz36TlxTUbRGa$grgVVlGe96IkgpplBsh5g$q1sbgYyRzT$Q9b$KC$0fY3Y$FgtxceI513fcf-xdG69FYBreIS7xFGWtt5SzyuO1vdG2Q6+KUg$R5r2JF7G3dCrfKm9F5W6SNo8oJxiYb$F9F2mXSxGQdNjOifjsCXv-y2HpmRix-7J$R9fQ$IyCVcjdldJyW5ezBaaSX51n618+$cmKjwjwdoz5IyD-lj4ubdu2ooVN5mzxHbdugAnITtOMsn21ok9EjT2szH0afmMvtipxB0yf17NL6E-ghmGgfCPHTx8CBzK17M61x3xu8hiwV4ulgulMHGA$apTuadT3yKoCzPU24SV$MvU-+zGe9KGwg2Nqi22lOXllz9frYouQOIaC1$tdYY6prieeE6+$XQowDTREXKCleJQVuc3I+ebdgUllcU3k7-6LCeFDyH-1cBgaD$wRk9K$pPB5T-bHumNQULt8fOIh1gg11V22lWmqd7rze3QyiQH4E56vtgHRT0OReOyvxn7EbzHS6TGx9rHexXgGa2oGF6vVj4QLtHEr6Skx0VuQfax8e4yD-i5L$c7VPf2YN2zBrMMjx0g95o-JAJ52qH031CB-itGsnTbBa3S8N6RWg5T803xjR8q9Ja6jdD$eq6-1tIo5wris1$+26XJId2c4lXqf6b$J8Ewm45sfy7GGJ8LwmAee2w8pG3vm4PpiXXojtJga9WpisgigxtFkwN4AIeOcyH12xwWwcclMmRxHg9o$fAm6UySDzx$9LwlhxWyTN2eswonH5evxv-9tCjHB3iotXYj0I11W+HvOTO98E9PBf3Ol3SVyzdaPB1+1nOzJUvdi8$1DcS$8$3Q8zfBntaq2Yx5-1z81K7HAeLrd-UvmzP4De3YXove7v$gwBVK77UjvzlqMQeJeQEASudU1qceYESNT8qzM1eVpi3Y28B6zfB+-RDaqJ4fDzsbqRTNat8p7PvQomzanz5Mdm9rPBQu1BS+X8vCeDzP4SjNa7GRj2A-Lw2SXe$lU8z+orid0ozYtVwVs$fVcUdJRhRc5g$1cPC5MNe23xYKI5cvoKOfrz0KME$yRx5bthmgIMxjcdgYHeh9mVItKCPN6XyvRnPXwjlOzpmXh3xkpFUl9BJclMMzM8QK8Q$FXItwnvpJSCOiT5A8DzvnffGiafeFBezTyNXO6NcMlbAnaU8iKimAXvTAnQGA08Os5q9Mgt16A6n-gyezemnmmLCIX$7qkD3mXws6-Pg2qAmLQh$BGIiiyNS8+F+BmfPulzqRDonJ3c-+pvo7rUErsBwr3P2-Ay2ErPBz328vzqxhil7oKhnIpUcHjRNqur+yKuKdFN8g7G18RKi927hR$tR4Nxu4kAaMf1B6gafM$IXX$BwrU-7ds$DEtgQDLnPoDzRX$C-gI1673uVBJuSvpkzFy9a47xYfyevyTBb7Ee5uqg$a58x$BlHsKHhpk-NyzS2esi3$WFMjK2cVTtGnXQ9+mBn$yHQHogfg63ynGjSbqeHEda$QMmrdLqabPdF03xL2y6$ArWvYjE5JRqsX7OaVOhy3ACoemueB26M6BD-OUEWhlMUq0WD2B$gTiukCfy$kPz$BIjBQUX532hl8mXvMMKoAE6mVf1aj6Hrk2GTPVNuDuBHU2h$EUaDgFhmHXRA8T72QDFBJg43JO2u72ObvErOqbE7N4fRAo+Sh2vD7j+QCxy46gl8ecQzHx8x3HFQH$5J3HSQczBa$La2HVD$BUMw-e5vDynygba+HBd3DjNBSpq$70d4gVEh$XpI$zHelcDktfcxRcpH7ddDXm5o$7M8Vbbj4Ba5sScYpbTXO9bgSoan4pGBELFcG$7evGB94UNw8j+8HvT7zGQjy0us9mg4jTRIWpGlPRivcYbTQeyWSH$80Gl$9x6vDCfQCX$U716smAOitq3bU76d9MQOuPaAXdomSBisqLMFnBvY16+evnaaqrXUl-6OOnBRB74mwVLrRroPC8gkc0Va2YVXB-QR6ofoRwYG9eyoyY-$Q4L+IXV$UHpjVzg7LryuOwg1MR7hWcaPXrqpRxRTYvNIhVwurRHKXbvetkI3JEhafTqvetY6ypLeaH08WOySUPFlHa-UIfgyTQQ8-A20eNgPtvtaXbJ-DyrJOx$tQ2gVVWD7b5$cMT8-WaTTAOnILUPrgWax3Ym74gkC0gixcFIkl2zRAtK1eyOBo5l4vBSdx2+$TILbfRAWKl$xMj9bjwb+MDlxGe$62nfb8+A1uze279lYYQiLowkyn1v0DYPKVq2wO57z6kbQjDItUOL7R+Jm+5gXKUOmik2uslvIcvrIMiEcGsEYfV6O21lOa8s9C4tBBydiVldVwggt7cpxOmG9S4f8hMdYdRG+itagJrvfm30o83ncubEGUJbba5Of5EXFNNVVUO5LbuTxrBsmDAFYpAlEqdKB$4tYBWLbjJbugkNYapHPdGBq2nkMAk1HxacJfh8n2A6$fs9fL2Hw8iA9eYGfr8GKrS7SuaOB+oahhT3kVDDY-XEEcQG9mrOPO3XHg3$PVKlCP-MP3u0wskb0tQYa5cgCUw4WA9txsscpHy9ecb4PCf3OpuwbTzRCPAWodBJwQVXxz2usi1ck28n3A4BWr+4gANPRvF9eM+P4L2HgkhqEQjax6-gy04$A+Pu3PI-vKj4byFB0jEFGf9NNdVoky7OrA-96$h6km8EC$zHfoxXnS0xi1YDA-QNj98kBB$eHQBKYv+JmWzHDs+KBfSDgB+P$Nwe13SYm$RhyID$2vnrNmbj4yP1Hu$mTL9EV7McueifVj8bRYyW96GW70FOk+A1$DkS4fTzRtv7scwivg2tMzlLdxduLwOibG5$grLzl+8n25TSyNUbrVD31HYYbFGYGJqbVDDz70JN-sK3NugTRejK5V3A+Wdaf$QjeWt-IdgEl$gg-RTK7jp92JmpT+EO3p2saBTcLTglS0wxRlaqmReK$nGzdPa5$7m7b3ubltpRoV758+6H$75+QH71n18pbPzcObsOIBurRndAFjr3tvMVHSFjm287ANzNy65Fm0Svb-G1zzoNAD4N54X1oPePXAM6HHIdOYYqmCfGpyXgT$vk1-GT$LNQMso2NVqiyOBNaWEjmYu+mDbJVe6sPhIeQ5jca7P1gg$05itoYY$5tYk1eV8K$yll$DxhCdudNtMNRNpza2mf2z5$fho2vC1zS$e3Mh-BVahCUU0NYRhz2+op1-$XjmVf1$x9$EcDwID6f12231Vj$dyla4Dawmgxy-kjbX78c3myqj$5g56m6adsNdUtKFApCjK-TEI+ygIEB3PcU$D7tFHRpGyslijw5at8FHj2mVN6S$2SWVOUduBwohC1-RV7izkvTawj3rg0AKAusFo2C6nq348W3+53Tv5$HgtDl4AAsFJUU2Ol0sC1f93vJrv1by9hzMxBXyShQIBgxPUVuG8y3Xp$B6-cDly6$2zupHyXyelD0$FzMPcjT0xe25dp3m5BYC8mfJCekkQxLo6S2xzxYnlId+aavMbxDhxFgv2+G$RTTrQLFrpqEgAMf9thelDeg6$O3k7pDEyxNncOYOxqCbxNMjCKQOoyCqrr$CcoCnMOyJH$GneSwKI4zoRRhhDPp4LbefYhDh0nzpXlfV$r5whRntl8mBzYGEDyO8wDbRTXuLl0hsbfRxEQOoyoE-SkXmpBX3-CBvXyRyS6cIm$dqxD6MgYpjlEs-qxl18mryoOUHnxp$-wdBQo5UVRj9U9+80Ul25T8CH2cdd0XWIxr8KjjKFLvg2bKff2shDinVg2Ci9HDeGWkUHe$0ViVpshlHqT6$M82zmS$XH6S$$hVPDGlcSr034$MGYClFQMYHEgCLPyXyf8YU2+kH9+D0j8rKzVrTa1UEyy9YrAlSHDUssy7+7+XoU3aaInXLbAgY4d4nar-QLOzmSLBJjMpo7T1J-DadkwEAKf$icY15$WjlhYOigAszixUYd9HJyLlu-msLKJBi4t9Uy+RF2KxK9EEmYqT6S7M$$vu7fcVwp$2DUWfVCJlI2$B9zIeQw73BwTY7lXRy$fEneQQcX5i++1Fqfb6mDpp$U49Ao5hSqOvWlElb2jqYU8UJBoHIRvkzlSrVTapAebjUeNQ$2+tM1QVfE730Xmzp6tHgaNrlmAmzfyvrOUbqVTI7xoJHk4dV890oOvqeFqM0Vy60R2zLPCh1AMxDxSH7vGOfAz$1KTysijs$z2f20jqgmXyRyyHplKVU4UnRXm-7dXKVenAod8HsTkdsOGV-IOF5aI1dQD+XpN$$$yXeK$LjmMHUHfJByQ6mX5fcPDcmbeWIPjmIRaHJ$jcOABvphx3Qw7sK3$nSctH$2Kp$$5yTlt2v2w6a$$$gjCLFSQ$BFFmhpnbV4K$VBFhqaw$i2NDXjxX$$le4Kozv$lESuie$kbMe8aEtl7m1djC9UlYnVHpP7xFtA4Viordtmlsj68X2$c9CcmpVDC$uX54zoXOmjrCGfwJWUtdDlbmoT44823bmdsp7lsj5noQk0ThxSyo$CXuj$7186+xL$AFWj5l$S3DCtfY5km0w4jsFCYf48rR0YHesBCI$-5hRt7nl3yS7fMwabh5PU38CnfdJXYhj$o3qCMu4JqY-MmU3SVWfo$yrhpPmsED+$fNkbFEm83W$dmIABx$zHy$$$zmRA3P4ItOYQLjcwU14djfDj0Hc7$$ARnvHtrtCAVBhQBT2YKyeIBcn1H$LpQfOzAxR3HUPJGzihImX7m5JmAsojC-FDWjPnB3t$XLRbjVyR9p0-465egSK9GI$fyzDipPeLsyz2a6Ob5DBXd8xgVudByDDaXd8$b2n3og2yB$f1HNfE$j$Nho$LQl7mIsND6$5y7wlVH9dKDrtrigzLQ3gJ1earLtDXJs20$fYCmHPbdH628dYVDXpMhqt7HSJbIrt86VK6q3Upfc0+n8YdW$0t$zD4zYoOjUbbOrNl5e$$BOB7MA-$5Q$9DDm$3D$u$cSs9Sg73dTbPBKn08OUnM6zDl6eqe6$$m0D$$",
    "s": "0.4712002860366456:1695186422:K0M-xPcYVQaQY95YwwVcbyjGnoK9lFZjUiIcEDd2Wmk"
    }
    cookies = ""
    headers = {
        "Host": "chat.aivvm.com",
        "Method": "POST",
        "Path": "/cdn-cgi/challenge-platform/h/g/jsd/r/80bac2c83a378cf5",
        "Scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.6",
        "Content-Length": "15521",
        "Content-Type": "application/json",
        "Cookie": f"cf_clearance={cookies}",
        "Origin": "https://chat.aivvm.com",
        "Sec-Ch-Ua": '"Brave";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"macOS"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Gpc": "1",
        "User-Agent": ua.random
    }
    # check if cookies is already in file
    cookies = check_or_make_cookies_file()
    if cookies:
        return cookies
    
    # if not already in file
    res = requests.post(url, data=payload)
    if res.status_code == 200:
        cookies =  res.cookies["cf_clearance"]
        res = requests.post(url, data=payload,headers=headers)
        if res.status_code == 200:
            cookies = res.cookies["cf_clearance"]
            if cookies:
                # write cookies to file
                check_or_make_cookies_file(cookies)
                return cookies
            return None
        else:
            return None
    else:
        return None


