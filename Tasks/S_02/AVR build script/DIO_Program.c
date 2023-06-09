/*Inclusions*/
/*Include Header files from LIB Layer*/

#include "STD_TYPES.h"
#include "BIT_MATH.h"

/*Inclusion for my own header files*/
#include "DIO_Interface.h"
#include "DIO_Private.h"
#include "DIO_Config.h"

/******************************************************************/
/*Func. Name: DIO_voidSetPinValue                                 */
/*i/p arguments: Copy_u8PortId options: PORTA, PORTB, PORTC, PORTD*/
/*Copy_u8PinId: PIN0, PIN1, PIN2, PIN3, PIN4, PIN5, PIN6, PIN7    */
/*Copy_u8Value: LOW, HIGH                                         */
/*return: void                                                    */
/******************************************************************/
void DIO_voidSetPinValue(u8 Copy_u8PortId, u8 Copy_u8PinId, u8 Copy_u8Value)
{
    /*i/p validation*/
    if(Copy_u8PortId > PORTD || Copy_u8PinId > PIN7)
    {
        //Do Nothing
    }
    else
    {
        switch(Copy_u8Value)
        {
            case LOW:   switch(Copy_u8PortId)
                        {
                            case PORTA: /*Action*/
                                        CLR_BIT(PORTA_REG,Copy_u8PinId);
                                        break;
                            case PORTB: CLR_BIT(PORTB_REG,Copy_u8PinId);
                                        break;
                            case PORTC: CLR_BIT(PORTC_REG,Copy_u8PinId);
                                        break;
                            case PORTD: CLR_BIT(PORTD_REG,Copy_u8PinId);
                                        break;
                            default:
                                        break;              
                        }
                        break;
            case HIGH:  switch(Copy_u8PortId)
                        {
                            case PORTA: /*Action*/
                                        SET_BIT(PORTA_REG,Copy_u8PinId);
                                        break;
                            case PORTB: SET_BIT(PORTB_REG,Copy_u8PinId);
                                        break;
                            case PORTC: SET_BIT(PORTC_REG,Copy_u8PinId);
                                        break;
                            case PORTD: SET_BIT(PORTD_REG,Copy_u8PinId);
                                        break;
                            default:
                                        break;              
                        }
                        break;
            default:    
                        break;
        }
    }
}

/******************************************************************/
/*Func. Name: DIO_voidSetPinDirection                             */
/*i/p arguments: Copy_u8PortId options: PORTA, PORTB, PORTC, PORTD*/
/*Copy_u8PinId: PIN0, PIN1, PIN2, PIN3, PIN4, PIN5, PIN6, PIN7    */
/*Copy_u8Direction: INPUT, OUTPUT                                 */
/*return: void                                                    */
/******************************************************************/
void DIO_voidSetPinDirection(u8 Copy_u8PortId, u8 Copy_u8PinId, u8 Copy_u8Direction)
{
    /*i/p validation*/
    if(Copy_u8PortId > PORTD || Copy_u8PinId > PIN7)
    {
        //Do Nothing
    }
    else
    {
        switch(Copy_u8Direction)
        {
            case INPUT:   switch(Copy_u8PortId)
                        {
                            case PORTA: /*Action*/
                                        CLR_BIT(DDRA_REG,Copy_u8PinId);
                                        break;
                            case PORTB: CLR_BIT(DDRB_REG,Copy_u8PinId);
                                        break;
                            case PORTC: CLR_BIT(DDRC_REG,Copy_u8PinId);
                                        break;
                            case PORTD: CLR_BIT(DDRD_REG,Copy_u8PinId);
                                        break;
                            default:
                                        break;              
                        }
                        break;
            case OUTPUT:  switch(Copy_u8PortId)
                        {
                            case PORTA: /*Action*/
                                        SET_BIT(DDRA_REG,Copy_u8PinId);
                                        break;
                            case PORTB: SET_BIT(DDRB_REG,Copy_u8PinId);
                                        break;
                            case PORTC: SET_BIT(DDRC_REG,Copy_u8PinId);
                                        break;
                            case PORTD: SET_BIT(DDRD_REG,Copy_u8PinId);
                                        break;
                            default:
                                        break;              
                        }
                        break;
            default:    
                        break;
        }
    }
}

/******************************************************************/
/*Func. Name: DIO_u8GetPinValue                                   */
/*i/p arguments: Copy_u8PortId options: PORTA, PORTB, PORTC, PORTD*/
/*Copy_u8PinId: PIN0, PIN1, PIN2, PIN3, PIN4, PIN5, PIN6, PIN7    */
/*return: unsigned char                                           */
/******************************************************************/
u8   DIO_u8GetPinValue(u8 Copy_u8PortId, u8 Copy_u8PinId)
{
    u8 Local_u8Variable;
    switch(Copy_u8PortId)
    {
        case PORTA: Local_u8Variable = GET_BIT(PINA_REG, Copy_u8PinId);
                    break;
        case PORTB: Local_u8Variable = GET_BIT(PINB_REG, Copy_u8PinId);
                    break;
        case PORTC: Local_u8Variable = GET_BIT(PINC_REG, Copy_u8PinId);
                    break;
        case PORTD: Local_u8Variable = GET_BIT(PIND_REG, Copy_u8PinId);
                    break;
        default:    
                    break;
    }
    return Local_u8Variable;
}


/******************************************************************/
/*Func. Name: DIO_voidSetPortValue                                */
/*i/p arguments: Copy_u8PortId options: PORTA, PORTB, PORTC, PORTD*/
/*Copy_u8Value: unsigned 8-bit value  (0x00-0xFF)                 */
/*return: void                                                    */
/******************************************************************/
void DIO_voidSetPortValue(u8 Copy_u8PortId, u8 Copy_u8Value)
{
    switch(Copy_u8PortId)
    {
        case PORTA: PORTA_REG = Copy_u8Value;
                    break;

        case PORTB: PORTB_REG = Copy_u8Value;
                    break;

        case PORTC: PORTC_REG = Copy_u8Value;
                    break;

        case PORTD: PORTD_REG = Copy_u8Value;
                    break;
        default:
                    break;
    }
    
}

/******************************************************************/
/*Func. Name: DIO_voidSetPortDirection                            */
/*i/p arguments: Copy_u8PortId options: PORTA, PORTB, PORTC, PORTD*/
/*Copy_u8Direction: INPUT, OUTPUT (0x00, 0xFF)                    */
/*return: void                                                    */
/******************************************************************/
void DIO_voidSetPortDirection(u8 Copy_u8PortId, u8 Copy_u8Direction)
{
        switch(Copy_u8Direction)
        {
            case INPUT:     
                        switch(Copy_u8PortId)
                        {
                            case PORTA: CLR_REG(DDRA_REG);
                                        break;
                            case PORTB: CLR_REG(DDRB_REG);
                                        break;
                            case PORTC: CLR_REG(DDRC_REG);
                                        break;
                            case PORTD: CLR_REG(DDRD_REG);
                                        break;
                            default:
                                        break;
                        }
                        break;
            case OUTPUT:
                        switch(Copy_u8PortId)
                        {
                            case PORTA: SET_REG(DDRA_REG);
                                        break;
                            case PORTB: SET_REG(DDRB_REG);
                                        break;
                            case PORTC: SET_REG(DDRC_REG);
                                        break;
                            case PORTD: SET_REG(DDRD_REG);
                                        break;
                            default:
                                        break;
                        }
                        break;
            default:
                            break;
        }
    
}


/******************************************************************/
/*Func. Name: DIO_u8GetPortValue                                  */
/*i/p arguments: Copy_u8PortId options: PORTA, PORTB, PORTC, PORTD*/
/*return: unsigned 8-bit value  (0x00-0xFF)                       */
/******************************************************************/
u8   DIO_u8GetPortValue(u8 Copy_u8PortId)
{
    u8 Local_u8PortState;
    
    if(Copy_u8PortId>PORTD)
    {/*do nothing*/}
    else
    {
        switch (Copy_u8PortId)
        {
            case PORTA: Local_u8PortState = PINA_REG;
                break;
            case PORTB: Local_u8PortState = PINB_REG;
                break;
            case PORTC: Local_u8PortState = PINC_REG;
                break;
            case PORTD: Local_u8PortState = PIND_REG;
                break;

            default:
                break;
        }
    }

    return Local_u8PortState;
}