class OmniCreate:
    def removeDuplicate(self, ekahs, index, output):
        if index == len(ekahs):
            print(output)
            return
        if ekahs[index] not in output:
            output += ekahs[index]
            self.removeDuplicate(ekahs, index + 1, output)
        else:
            self.removeDuplicate(ekahs, index + 1, output)


create = OmniCreate()
print(
    create.removeDuplicate(
        "qoiueoiruoieytuieyiweyriqyiyeuiryieyriueyireuyieuryiewyruie", 0, ""
    )
)
